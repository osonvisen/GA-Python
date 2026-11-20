import mysql.connector

from config_local import DB_CONFIG
from models import Product, Customer, Employee


# ------ PRODUCTS ------
def get_products():
    sql = """
            SELECT id, name, description, monthly_price
            FROM product
            ORDER BY name
    """

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append(Product(row[0], row[1], row[2], row[3]))
    return products


def get_product(product_id):
    sql = """
        SELECT id, name, description, monthly_price
        FROM product
        WHERE id = %s
    """
    params = (product_id,)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            rows = cursor.fetchall()
    for row in rows:
        if row is None:
            return None
        return Product(row[0], row[1], row[2], row[3])

def insert_product(name, description, monthly_price):
    sql = """
        INSERT INTO product (name, description, monthly_price)
        VALUES (%s, %s, %s)
    """
    params = (name, description, monthly_price)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()




# ------ CUSTOMERS ------
def get_customers():
    sql = """
            SELECT c.id, c.first_name, c.last_name, c.email, c.phone, c.product_id, p.name
            FROM customer c
            JOIN product p ON p.id = c.product_id
            ORDER BY c.last_name, c.first_name
    """

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

    customers = []
    for row in rows:
        customers.append(Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    return customers


# ------ EMPLOYEES ------
def get_employees():
    sql = """
            SELECT id, first_name, last_name, role, email
            FROM employee
            ORDER BY last_name, first_name
    """

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

    employees = []
    for row in rows:
        employees.append(Employee(row[0], row[1], row[2], row[3], row[4]))
    return employees