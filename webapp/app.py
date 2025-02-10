import asyncio
import contextlib
from functools import wraps
import json
import time
from flask import Flask, jsonify, make_response, redirect, render_template, request, g, session, url_for
import plotly.graph_objects as go

# import webapp.example
# from . import example
# from .example import Example
# from .. import dziedziczenie  # nie zadziała
# from ..dziedziczenie import Dog  # nie zadziała
from .submodule import subtest
from game.main import iter_cards_at, prepare_cards, run_turn

from webapp.views.game import game_view  # bez blueprint
from webapp.views.game import bp as bp_game
from webapp.db import get_db

def create_app():
    app = Flask(__name__)
    app.config.from_object("webapp.default_config")
    with contextlib.suppress(ImportError):
        app.config.from_object("webapp.config")
    app.config.from_prefixed_env()
    # e.g. export FLASK_COMPANY_NAME="Fiasco Sp.z.o.o."
    with contextlib.suppress(FileNotFoundError):
        app.config.from_file("config.json", load=json.load)

    with app.app_context():
        # get_db().append_cards([...])
        ...  # DB init code here

    def funny_name(name: str) -> str:
        return name[::-1].title()

    @app.context_processor
    def standard_context():
        print(app.config)
        return dict(
            company_name=app.config["COMPANY_NAME"],
            iter_cards_at=iter_cards_at,
            # Funkcje też można tu przekazać
        )

    app.jinja_env.filters["funny_name"] = funny_name
    app.jinja_env.add_extension("jinja2.ext.loopcontrols")

    @app.before_request
    def check_request():
        # g.username = request.cookies.get('username', "Unknown")
        g.username = session.get('username', "Unknown")
        if g.username == "admin":
            g.user_roles = ["reader", "admin"]
        else:
            g.user_roles = ["reader"]
        is_user_local = (request.remote_addr == "127.0.0.1")
        g.is_user_local = is_user_local


    def admin_role_needed(view):
        @wraps(view)
        def decorated_view(*args, **kwargs):
            if "admin" not in g.user_roles:
                return "You have no permissions. Your roles are: " + str(g.user_roles)
            return view(*args, **kwargs)
        return decorated_view

    @app.get("/delay")
    def delayed():
        time.sleep(5)
        return "<h1> OK \n"

    # pip install flask[async]
    @app.get("/delay_a")
    async def delayed_a():
        a, b = await asyncio.gather( asyncio.sleep(5),  asyncio.sleep(5) )
        return "<h1> OK \n"


    @app.get("/plot")
    def plot():
        fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4], y=[54, 23, 65, 12]))
        fig_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        return f"<html><h1>Plot</h1>{fig_html}"

    @app.get("/login")
    def login_form():
        return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=password name=password>
                <p><input type=submit value=Login>
            </form>
        '''

    @app.post("/login")
    def login():
        # response = make_response("<h1>OK")
        # response.set_cookie('username', request.form['username'])
        # return response
        session["username"] = request.form['username']
        return redirect(url_for("home"))

    @app.get("/administration")
    @admin_role_needed
    def administration():
        return "<h1>This is admin page"

    @app.route("/")
    def home():
        # from pprint import pprint
        # pprint(vars(request))
        name = g.username
        print("Hello", name)
        if 'is_user_local' in g and g.is_user_local:
            name += " (local)"
        other_names = ["Ania", "Karol", "Kasia"]
        return render_template(
            "home.html.j2",
            name=name,
            paragraph_count=4,
            other_names=other_names,
        )

    @app.route("/name/<name>")
    def greetings(name):
        other_names = ["Ania", "Karol", "Kasia"]
        return render_template(
            "home.html.j2",
            name=name,
            paragraph_count=4,
            other_names=other_names,
        )

    # Bez blueprint (dwie opcje):
    # app.route("/game", methods=["GET", "POST"])(game_view)
    # app.add_url_rule("/game", view_func=game_view, methods=["GET", "POST"])

    app.register_blueprint(bp_game, url_prefix="/game", options={"color": "red"})


    @app.get('/api/game/cards')
    def get_cards_api():
        data = [c.to_dict() for c in cards]
        # return json.dumps(data)
        # return jsonify(data)
        return data

    # curl -v -X POST -d '{"move": "up"}' --header "Content-Type: application/json" localhost:5000/api/game/move
    @app.post('/api/game/move')
    def do_movement_api():
        # data = request.get_data()
        # json.loads(data)
        data = request.get_json()
        # TODO implement movement and do_turn
        return "TODO"

    # curl -N localhost:5000/steam-test
    @app.get("/steam-test")
    def stream_test():
        import time
        for x in range(20):
            yield f"--{x}--"
            time.sleep(0.1)

    # Using Click framework
    @app.cli.command("init-db")
    def init_database():
        get_db().append_cards([...])
        print("After init there are", len(get_db().get_cards()), "cards")

    return app

if __name__ == "__main__":
    create_app().run(debug=True)  #, use_reloader=False
