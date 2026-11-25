import database
from flask import Flask, abort, redirect, render_template, request
from models import City
from mysql.connector import Error

app = Flask(__name__)


# OPPGAVE 5 and 7: add and edit read the same four fields, so we write it once.
# This function only fetches the text. The rules are in City.from_form().
def read_city_form():
    return City.from_form(
        request.form.get("name", ""),
        request.form.get("country_code", ""),
        request.form.get("district", ""),
        request.form.get("population", "")
    )


# EKSTRAOPPGAVE B: catches database errors from all routes, so no route needs its own try/except.
# The details go to the log. The user only gets a short message.
@app.errorhandler(Error)
def database_error(error):
    app.logger.exception("Database error")
    return "Database unavailable", 503


@app.route("/")
def index():
    return redirect("/cities")


@app.route("/cities")
def cities():
    code = request.args.get("country", "NOR").strip().upper()
    if not City.is_country_code(code):
        return "Invalid country code. Use three letters, for example NOR.", 400
    return render_template("cities.html", code=code, rows=database.get_cities(code))


# OPPGAVE 4
@app.route("/city/<int:city_id>")
def show_city(city_id):
    city = database.get_city(city_id)
    if city is None:
        abort(404)
    return render_template(
        "city_form.html",
        city_id=city.id,
        name=city.name,
        country_code=city.country_code,
        district=city.district,
        population=city.population
    )


# OPPGAVE 4 (GET), 5 and 6 (POST)
@app.route("/add", methods=["GET", "POST"])
def add_city():
    if request.method == "GET":
        # city_id=None tells the template that this is a new city: no ID and no delete button.
        return render_template("city_form.html", city_id=None, name="",
                               country_code="NOR", district="", population=0)

    try:
        city = read_city_form()
    except ValueError as error:
        return str(error), 400

    # EKSTRAOPPGAVE A: the format is right, but does the country exist?
    if not database.country_exists(city.country_code):
        return "Unknown country code.", 400

    database.insert_city(city.name, city.country_code, city.district, city.population)
    return redirect("/cities", code=303)


# OPPGAVE 7
@app.route("/edit/<int:city_id>", methods=["POST"])
def edit_city(city_id):
    try:
        city = read_city_form()
    except ValueError as error:
        return str(error), 400

    # EKSTRAOPPGAVE B: None means the city is missing (404).
    # A database error raises an exception instead, and ends up in database_error() (503).
    if database.get_city(city_id) is None:
        abort(404)

    # EKSTRAOPPGAVE A
    if not database.country_exists(city.country_code):
        return "Unknown country code.", 400

    # The ID comes from the URL, never from the form, so the user cannot change it.
    database.update_city(city_id, city.name, city.country_code, city.district, city.population)
    return redirect("/cities", code=303)


# OPPGAVE 8
@app.route("/delete/<int:city_id>", methods=["POST"])
def remove_city(city_id):
    database.delete_city(city_id)
    return redirect("/cities", code=303)


if __name__ == "__main__":
    app.run(debug=True, port=5001)  # 5001 because AirPlay often uses 5000 on Mac
