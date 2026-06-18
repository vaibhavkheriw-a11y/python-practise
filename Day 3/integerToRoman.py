# Write a Python class to convert an integer to a roman numeral.

class IntegerToRoman:
    def convert(self, number):
        roman_values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman_number = ""

        for value, symbol in roman_values:
            while number >= value:
                roman_number += symbol
                number -= value

        return roman_number


converter = IntegerToRoman()
print(converter.convert(590))
