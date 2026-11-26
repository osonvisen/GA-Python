from mysql.connector import IntegrityError
from mysql.connector.errorcode import ER_ROW_IS_REFERENCED

import database
from flask import Flask, render_template, request, redirect
from decimal import Decimal, InvalidOperation

app = Flask(__name__)

def form_text(name):
    return request.form.get(name, "")


def read_product_form():
    name = form_text("name")
    description = form_text("description")

    try:
        monthly_price = Decimal(form_text("monthly_price"))
    except InvalidOperation:
        return "Invalid price!"

    if not name or len(name) > 50:
        return None, "Invalid product name"

    if not description or len(description) > 200:
        return None, "Description too long!"

    if monthly_price > 999999 or monthly_price <= 0:
        return None, "Invalid price!"

    return (name, description, monthly_price), None


@app.route("/")
def index():
    return render_template("index.html", heading="Fjordform")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/products")
def products():
    return render_template("products.html", rows=database.get_products())


@app.route("/product/<int:product_id>")
def show_product(product_id):
    product = database.get_product(product_id)
    if product is None:
        return "Product not found!", 404
    return render_template("product_form.html", product=product)


@app.route("/product/add", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template("product_form.html", product=None)

    values, error = read_product_form()
    if error:
        return error, 400
    database.insert_product(*values)
    return redirect("/products", code=303)


@app.route("/product/<int:product_id>/edit", methods=["POST"])
def edit_product(product_id):

    values, error = read_product_form()
    if error:
        return error, 400
    database.update_product(product_id, *values)
    return redirect("/products", code=303)


@app.route("/product/<int:product_id>/delete", methods=["POST"])
def remove_product(product_id):
    try:
        database.delete_product(product_id)
    except IntegrityError as error:
        if error.errno == ER_ROW_IS_REFERENCED:
            return "Product is in use", 409
    return redirect("/products", code=303)



@app.route("/customers")
def customers():
    return render_template("customers.html", rows=database.get_customers())


@app.route("/employees")
def employees():
    return render_template("employees.html", rows=database.get_employees())

if __name__ == "__main__":
    app.run(debug=True, port=5001)