import sys

import mysql.connector
from mysql.connector import Error

# OPPGAVE 8

region = input("Enter a region: ")

# Validate the number BEFORE we connect, so an invalid value never reaches the query.
try:
    min_population = int(input("Enter a minimum population: "))
except ValueError:
    print("The minimum population must be a whole number, for example 10000000.")
    sys.exit(1)

if min_population < 0:
    print("The minimum population cannot be negative.")
    sys.exit(1)

try:
    with mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="gokstad",
        database="world"
    ) as connection:
        print("Connected successfully")
        with connection.cursor() as cursor:
            sql = (
                "SELECT Name, Population "
                "FROM country "
                "WHERE Region = %s AND Population >= %s "
                "ORDER BY Name "
            )
            # The values are sent in the same order as the %s placeholders appear in the SQL.
            cursor.execute(sql, (region, min_population))
            rows = cursor.fetchall()

            if not rows:
                print("No countries found for this region and minimum population!")
            else:
                for name, population in rows:
                    print(f"{name}: {population}")
                print(f"Found {len(rows)} countries in this region.")

except Error as error:
    print(f"Error using MySQL: {error}")

# Why parameterise even though min_population is validated?
# Validation only covers min_population. region is still raw user input and could contain SQL.
# Parameterisation keeps data and SQL separate for every value, so we don't have to remember
# which values happen to be "safe". It also handles quoting and types correctly.
