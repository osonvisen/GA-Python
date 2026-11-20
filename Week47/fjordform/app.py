import database
from flask import Flask, render_template, request, redirect
from decimal import Decimal, InvalidOperation

app = Flask(__name__)

def form_text(name):
    return request.form.get(name, "")

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
    name = form_text("name")
    description = form_text("description")

    try:
        monthly_price = Decimal(form_text("monthly_price"))
    except InvalidOperation:
        return "Invalid price!"

    if not name or len(name) > 50:
        return "Invalid prodcut name", 400

    if not description or len(description) > 200:
        return "Description too long!", 400

    if monthly_price > 999999 or monthly_price <= 0:
        return "Invalid price!", 400

    database.insert_product(name, description, monthly_price)
    return redirect("/products", code=303)

@app.route("/customers")
def customers():
    return render_template("customers.html", rows=database.get_customers())


@app.route("/employees")
def employees():
    return render_template("employees.html", rows=database.get_employees())

if __name__ == "__main__":
    app.run(debug=True, port=5001)