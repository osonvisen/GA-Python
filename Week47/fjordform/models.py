class Product:
    def __init__(self, product_id, name, description, monthly_price):
        self.id = product_id
        self.name = name
        self.description = description
        self.monthly_price = monthly_price


class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, product_id, product_name=None):
        self.id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.product_id = product_id
        self.product_name = product_name


class Employee:
    def __init__(self, employee_id, first_name, last_name, role, email):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.email = email


