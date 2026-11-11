import mysql.connector
from mysql.connector import Error

# OPPGAVE 11


def search_languages(cursor, country_code):
    sql = (
        "SELECT Language, Percentage, IsOfficial "
        "FROM countrylanguage "
        "WHERE CountryCode = %s "
        "ORDER BY Language "
    )
    cursor.execute(sql, (country_code,))
    rows = cursor.fetchall()

    if not rows:
        print("No languages found for this country code!")
    else:
        for language, percentage, is_official in rows:
            print(f"{language}: {percentage}% (official: {is_official})")
        print(f"Found {len(rows)} language rows.")


try:
    # We connect once and reuse the same connection and cursor for every search,
    # instead of opening a new connection inside the loop.
    with mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="gokstad",
        database="world"
    ) as connection:
        print("Connected successfully")
        with connection.cursor() as cursor:
            while True:
                # strip() removes spaces, so input with only spaces also counts as empty.
                country_code = input("Enter a country code (empty to quit): ").strip()
                if not country_code:
                    break
                search_languages(cursor, country_code)
                print()

        print("Goodbye!")

except Error as error:
    print(f"Error using MySQL: {error}")
