class City:
    """One row from the city table in the World database."""

    # OPPGAVE 4 and 5: the limits come from SHOW CREATE TABLE city;
    # They belong to the class (not to one object), so they are written only once.
    MAX_NAME_LENGTH = 35          # CHAR(35)
    MAX_DISTRICT_LENGTH = 20      # CHAR(20)
    MAX_POPULATION = 2147483647   # The largest value a MySQL INT can hold

    # OPPGAVE 2
    def __init__(self, city_id, name, country_code, district, population):
        # A new city has no ID until MySQL has generated one, so None is allowed here.
        self.id = None if city_id is None else int(city_id)
        self.name = name
        self.country_code = country_code
        self.district = district
        self.population = int(population)

    # A static method needs neither self nor cls. It lives here because it is a rule about cities,
    # and both the form (Oppgave 5) and the city search use it.
    @staticmethod
    def is_country_code(code):
        # isalpha() alone accepts letters like Æ, so we also need isascii().
        return len(code) == 3 and code.isascii() and code.isalpha()

    # OPPGAVE 5
    # A class method is called on the class: City.from_form(...). It works like an extra constructor:
    # it takes raw text from the form, and either returns a valid City or raises ValueError.
    @classmethod
    def from_form(cls, name, country_code, district, population):
        name = name.strip()
        country_code = country_code.strip().upper()
        district = district.strip()

        if not name:
            raise ValueError("Name cannot be empty.")
        if len(name) > cls.MAX_NAME_LENGTH:
            raise ValueError(f"Name can be at most {cls.MAX_NAME_LENGTH} characters.")

        if not cls.is_country_code(country_code):
            raise ValueError("Country code must be exactly three letters, for example NOR.")

        # An empty district is allowed, so we only check the length.
        if len(district) > cls.MAX_DISTRICT_LENGTH:
            raise ValueError(f"District can be at most {cls.MAX_DISTRICT_LENGTH} characters.")

        # Form values are always text, also from type="number".
        try:
            population = int(population)
        except ValueError:
            # Replace Python's technical message with one the user understands.
            raise ValueError("Population must be a whole number.") from None
        if population < 0:
            raise ValueError("Population cannot be negative.")
        if population > cls.MAX_POPULATION:
            raise ValueError(f"Population can be at most {cls.MAX_POPULATION}.")

        return cls(None, name, country_code, district, population)


# OPPGAVE 2: short test. Runs only with "python models.py", not when database.py imports City.
if __name__ == "__main__":
    test_city = City(9999, "Testby", "NOR", "Vestfold", 1234)
    print(test_city.id, test_city.name, test_city.country_code,
          test_city.district, test_city.population)
