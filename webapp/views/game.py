from flask import Blueprint, current_app, g, render_template, request
from game.main import run_turn

bp = Blueprint("game", __name__)

cards = []
hero_movement = None

@bp.route("/scoreboard", methods=["GET", "POST"])
def scoreboard():
    return "<h1>Here be scoreboard"

@bp.route("/", methods=["GET", "POST"])
def game_view():
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
    print("OBJ G. USERNAME:", g.username)
    print("OBJ APP:", current_app)
    return render_template(
        "game/game.html.j2",
        cards=cards,
        board_size_x=15,
        board_size_y=15,
    )
