import mysql.connector
from mysql.connector import Error, cursor

# OPPGAVE 4
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
                "SELECT Language, Percentage, IsOfficial "
                "FROM countrylanguage "
                "WHERE CountryCode = 'SWE' "
                "ORDER BY Language "
            )
            cursor.execute(sql)
            rows = cursor.fetchall()

            if not rows:
                print("No languages found for this country code!")
            else:
                for language, percentage, is_official in rows:
                    print(f"{language}: {percentage}% (official: {is_official})")
                print(f"Found {len(rows)} language rows.")

except Error as error:
    print(f"Error using MySQL: {error}")

