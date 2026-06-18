# Write a Python program to generate a random alphabetical character, alphabetical string and alphabetical string of a fixed length. Use random.choice()

import random
import string


def random_character():
    return random.choice(string.ascii_letters)


def random_string():
    length = random.randint(1, 10)
    result = ""

    for _ in range(length):
        result += random.choice(string.ascii_letters)

    return result


def fixed_length_string(length):
    result = ""

    for _ in range(length):
        result += random.choice(string.ascii_letters)

    return result


print("Random alphabetical character - ", random_character())
print("Random alphabetical string - ", random_string())
print("Fixed length alphabetical string -", fixed_length_string(111))
