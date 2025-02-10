from functools import wraps
import json
import time
from flask import Flask, jsonify, make_response, redirect, render_template, request, g, session, url_for

# import webapp.example
# from . import example
# from .example import Example
# from .. import dziedziczenie  # nie zadziała
# from ..dziedziczenie import Dog  # nie zadziała
from .submodule import subtest
from game.main import iter_cards_at, prepare_cards, run_turn

from webapp.views.game import game_view  # bez blueprint
from webapp.views.game import bp as bp_game

def create_app():
    app = Flask(__name__)
    app.secret_key = "--- Development-only key ---"


    def funny_name(name: str) -> str:
        return name[::-1].title()

    @app.context_processor
    def standard_context():
        return dict(
            company_name="Acme INC.",
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

    return app



if __name__ == "__main__":
    create_app().run(debug=True)  #, use_reloader=False
