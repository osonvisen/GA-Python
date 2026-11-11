import mysql.connector
from mysql.connector import Error, cursor

# OPPGAVE 6

region = input("Enter a region: ")

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
                "WHERE Region = %s "
                "ORDER BY Name "
            )
            cursor.execute(sql, (region,))
            rows = cursor.fetchall()

            if not rows:
                print("No languages found for this region!")
            else:
                for name, population in rows:
                    print(f"{name}: {population}")
                print(f"Found {len(rows)} countries in this region.")

except Error as error:
    print(f"Error using MySQL: {error}")