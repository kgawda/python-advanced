from flask import Flask, render_template

app = Flask(__name__)

def funny_name(name: str) -> str:
    return name[::-1].title()

@app.context_processor
def standard_context():
    return dict(
        company_name="Acme INC.",
        # Funkcje też można tu przekazać
    )

app.jinja_env.filters["funny_name"] = funny_name

@app.route("/")
def hello_world():
    name = "Konrad"
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

if __name__ == "__main__":
    app.run(debug=True)  #, use_reloader=False
