import mysql.connector
from mysql.connector import Error, errorcode

# OPPGAVE 10

try:
    with mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="gokstad",
        database="world_missing"  # Change back to "world" to check that the connection works again
    ) as connection:
        print("Connected successfully")

except Error as error:
    # errno is MySQL's error number. ER_BAD_DB_ERROR (1049) means "Unknown database".
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Could not connect: the database does not exist. Check the database name.")
    else:
        print(f"Error using MySQL: {error}")

# Difference between this error, ValueError (Oppgave 8) and no matches (Oppgave 4):
# - mysql.connector.Error: something went wrong talking to the database (wrong database,
#   wrong password, server not running). We never got to run the query.
# - ValueError: the user's input could not be converted to int. This is a Python error,
#   before the database is involved at all.
# - No matches: everything worked. The query ran successfully and the answer was simply
#   an empty list. That is a normal result, not an error.
