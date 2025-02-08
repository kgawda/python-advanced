import time
from flask import Flask, make_response, render_template, request, g

# import webapp.example
# from . import example
# from .example import Example
# from .. import dziedziczenie  # nie zadziała
# from ..dziedziczenie import Dog  # nie zadziała
from .submodule import subtest
from game.main import iter_cards_at, prepare_cards, run_turn

app = Flask(__name__)


hero_movement = None
def move_hero():
    return hero_movement

cards = prepare_cards(
    board_size_x=15,
    board_size_y=15,
    n_enemies=5,
    n_heroes=1,
    hero_kwargs={"movement_callback": move_hero},
)


def funny_name(name: str) -> str:
    return name[::-1].title()



def get_db():
    if '_db' not in g:
        g._db = ... # CreateDatabaseConnection(...)
    return g._db


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
    g.username = request.cookies.get('username', "Unknown")
    is_user_local = (request.remote_addr == "127.0.0.1")
    g.is_user_local = is_user_local

@app.get("/login")
def login_form():
    response = make_response("<h1>OK")
    response.set_cookie('username', "Henryk")
    return response

# @app.post("/login")
# def login():
#     ...


@app.route("/")
def hello_world():
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

@app.route("/game", methods=["GET", "POST"])
def game():
    global hero_movement
    if request.method == "POST":
        if "button_up" in request.form:
            hero_movement = "up"
        elif "button_down" in request.form:
            hero_movement = "down"
        elif "button_left" in request.form:
            hero_movement = "left"
        elif "button_right" in request.form:
            hero_movement = "right"
    else:
        hero_movement = None
    
    run_turn(
        board_size_x=15, board_size_y=15, cards=cards, sleep_time=0, print_target=None, min_cards=0,
    )
    return render_template(
        "game.html.j2",
        cards=cards,
        board_size_x=15,
        board_size_y=15,
    )

if __name__ == "__main__":
    app.run(debug=True)  #, use_reloader=False
