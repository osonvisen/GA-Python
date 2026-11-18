from flask import Flask, render_template, request
from Week46.Oppgave6 import get_cities

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", heading="Vårt hjørne på localhost")

@app.route("/about")
def about():
    return render_template("about.html", author="Ørjan")

@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest").strip()
    if not name:
        name = "Guest"
    try:
        int(name)
        name = "Det er ikke lov å hete et tall!"

    except ValueError as e:
        print(e)
    return render_template("greet.html", name=name)

@app.route("/cities")
def cities():
    code = request.args.get("country", "NOR").strip().upper()
    if len(code) != 3:
        return "Invalid country code. Only 3 letters allowed.", 400
    rows = get_cities(code)
    return render_template("cities.html", code=code, rows=rows)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
