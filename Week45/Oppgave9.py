import mysql.connector
from mysql.connector import Error

# OPPGAVE 9

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
            # Safe: %s is a placeholder, NOT string formatting. No quotes around it.
            # The driver sends region separately as data, so it can never become part of the SQL.
            sql = (
                "SELECT Name, Population "
                "FROM country "
                "WHERE Region = %s "
                "ORDER BY Name "
            )
            cursor.execute(sql, (region,))
            rows = cursor.fetchall()

            if not rows:
                print(f"No countries found for region: {region}")
            else:
                for name, population in rows:
                    print(f"{name}: {population}")
                print(f"Found {len(rows)} countries in this region.")

except Error as error:
    print(f"Error using MySQL: {error}")

# What could the input change in the unsafe version?
# With an f-string, the input becomes part of the SQL text. ' OR '1'='1 closes the string
# and adds a condition that is always true, so the query returns every country.
# Other input could change the query in other ways, and an apostrophe like in "O'Brien"
# simply breaks the SQL and causes an error.
#
# What does parameterisation do differently?
# The SQL text and the values are sent separately. The database parses the SQL first,
# then treats the value purely as data. ' OR '1'='1 is then just a (strange) region name
# with no matches.
#
# Is it safe to use an f-string in print()?
# Yes. print() only shows text to the user and doesn't execute anything.
# The danger is only when the f-string builds SQL (or other code) that gets executed.
