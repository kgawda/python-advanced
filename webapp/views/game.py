from flask import Blueprint, current_app, g, render_template, request
from game.main import prepare_cards, run_turn
from webapp.db import get_db

bp = Blueprint("game", __name__)

hero_movement = None
def move_hero():
    return hero_movement


@bp.route("/scoreboard", methods=["GET", "POST"])
def scoreboard():
    return "<h1>Here be scoreboard"

@bp.route("/", methods=["GET", "POST"])
def game_view():
    global hero_movement

    cards = get_db().get_cards()
    if not cards:
        cards = prepare_cards(
            board_size_x=15,
            board_size_y=15,
            n_enemies=5,
            n_heroes=1,
            hero_kwargs={"movement_callback": move_hero},
        )
        get_db().append_cards(cards)

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
        board_size_x=15,
        board_size_y=15,
        cards=cards,
        sleep_time=0,
        print_target=None,
        min_cards=0,
        card_remover=get_db().remove_card,
    )
    print("OBJ G. USERNAME:", g.username)
    print("OBJ APP:", current_app)
    return render_template(
        "game/game.html.j2",
        cards=cards,
        board_size_x=15,
        board_size_y=15,
    )
