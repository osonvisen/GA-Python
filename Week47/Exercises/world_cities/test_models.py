import unittest

from models import City

# Run: python -m unittest
# Needs no database, because the validation lives in City and not in the routes.


class TestCityFromForm(unittest.TestCase):
    def test_valid_input_is_cleaned_and_converted(self):
        city = City.from_form("  Testby ", " nor ", "", "1234")
        self.assertEqual(
            (city.id, city.name, city.country_code, city.district, city.population),
            (None, "Testby", "NOR", "", 1234)
        )

    def test_longest_allowed_values_are_accepted(self):
        City.from_form("a" * 35, "SWE", "b" * 20, "2147483647")

    def test_invalid_input_raises_value_error(self):
        invalid_inputs = [
            ("", "NOR", "", "1"),
            ("   ", "NOR", "", "1"),
            ("a" * 36, "NOR", "", "1"),
            ("Testby", "NO", "", "1"),
            ("Testby", "N0R", "", "1"),
            ("Testby", "NØR", "", "1"),
            ("Testby", "NOR", "b" * 21, "1"),
            ("Testby", "NOR", "", "abc"),
            ("Testby", "NOR", "", ""),
            ("Testby", "NOR", "", "-1"),
            ("Testby", "NOR", "", "2147483648"),
        ]
        for values in invalid_inputs:
            with self.subTest(values=values):
                with self.assertRaises(ValueError):
                    City.from_form(*values)


if __name__ == "__main__":
    unittest.main()
