import mysql.connector

from config_local import DB_CONFIG
from models import City


# ------ READ ------
def get_cities(code):
    sql = """
        SELECT ID, Name, CountryCode, District, Population
        FROM city
        WHERE CountryCode = %s
        ORDER BY Name
    """
    params = (code,)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            rows = cursor.fetchall()

    cities = []
    for row in rows:
        cities.append(City(row[0], row[1], row[2], row[3], row[4]))
    return cities


# OPPGAVE 3
def get_city(city_id):
    sql = """
        SELECT ID, Name, CountryCode, District, Population
        FROM city
        WHERE ID = %s
    """
    params = (city_id,)  # The comma makes this a tuple. (city_id) is just a number in parentheses.
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            row = cursor.fetchone()  # ID is the primary key, so there is at most one row.

    if row is None:
        return None
    # The order in SELECT must match the order in the constructor.
    return City(row[0], row[1], row[2], row[3], row[4])


# EKSTRAOPPGAVE A
def country_exists(code):
    # SELECT 1 is enough: we only need to know if there is a row, not what it contains.
    sql = """
        SELECT 1
        FROM country
        WHERE Code = %s
    """
    params = (code,)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchone() is not None


# ------ CREATE ------
# OPPGAVE 6
def insert_city(name, country_code, district, population):
    # No ID here: MySQL generates it (AUTO_INCREMENT).
    sql = """
        INSERT INTO city (Name, CountryCode, District, Population)
        VALUES (%s, %s, %s, %s)
    """
    params = (name, country_code, district, population)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()  # Without commit() the new row is lost when the connection closes.


# ------ UPDATE ------
# OPPGAVE 7
def update_city(city_id, name, country_code, district, population):
    sql = """
        UPDATE city
        SET Name = %s, CountryCode = %s, District = %s, Population = %s
        WHERE ID = %s
    """
    # Same order as the placeholders: four new values first, the ID last.
    params = (name, country_code, district, population, city_id)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()


# ------ DELETE ------
# OPPGAVE 8: the ID is enough to find the row, no matter how many fields City has.
def delete_city(city_id):
    sql = """
        DELETE FROM city
        WHERE ID = %s
    """
    params = (city_id,)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()
