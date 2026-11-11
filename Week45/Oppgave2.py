import mysql.connector
from mysql.connector import Error, cursor

# OPPGAVE 2
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
                "SELECT Language, Percentage "
                "FROM countrylanguage "
                "WHERE CountryCode = 'SWE' "
                "ORDER BY Language "
            )
            cursor.execute(sql)
            rows = cursor.fetchall()

            for language, percentage in rows:
                print(f"{language}: {percentage}%")

except Error as error:
    print(f"Error using MySQL: {error}")

