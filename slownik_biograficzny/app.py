from flask import Flask, abort, render_template

mock_db = {
    1: ("Jan Kochanowski", "Poeta renesansowy, znany z 'Trenów' oraz 'Odprawy posłów greckich'."),
    2: ("Mikołaj Kopernik", "Astronom, twórca teorii heliocentrycznej."),
    3: ("Maria Skłodowska-Curie", "Dwukrotna laureatka Nagrody Nobla, odkryła polon i rad."),
    4: ("Henryk Sienkiewicz", "Pisarz, laureat Nagrody Nobla, autor 'Quo Vadis'."),
}

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html.j2")

@app.route("/characters")
def character_list():
    return render_template("character_list.html.j2", character_list=mock_db)

@app.route("/characters/<int:character_id>-<junk>")
def character(character_id, junk):
    character = mock_db.get(character_id) or abort(404)
    return render_template("character.html.j2", character=character)
