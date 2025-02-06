from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "<i>Konrad</i>"
    return render_template(
        "home.html.j2",
        name=name,
        paragraph_count=4
    )

if __name__ == "__main__":
    app.run(debug=True)  #, use_reloader=False
