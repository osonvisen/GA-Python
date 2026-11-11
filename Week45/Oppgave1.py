import mysql.connector
from mysql.connector import Error

# OPPGAVE 1
try:
    with mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="gokstad",
        database="world"
    ) as connection:
        print("Connected successfully")

except Error as error:
    print(f"Error using MySQL: {error}")