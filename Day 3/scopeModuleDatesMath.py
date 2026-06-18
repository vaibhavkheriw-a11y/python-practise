# Scope, Module, Dates, Math

import datetime
import math
from integerToRoman import IntegerToRoman


# Scope example
message = "This is global variable"


def show_scope():
    message = "This is a local variable"

    print("Inside function:", message)
    print("Inside function:", )


show_scope()
print("Outside function:", message)


# Module example
converter = IntegerToRoman()
print(converter.convert(7))


# Dates example
today = datetime.date.today()
current_time = datetime.datetime.now()

print("Today's date:", today)
print("Current date and time:", current_time)
print("Current year:", current_time.year)
print("Current month:", current_time.month)
print("Current day:", current_time.day)


# Math example
number = 7.8

print("Ceil value:", math.ceil(number))
print("Floor value:", math.floor(number))
print("Factorial:", math.factorial(5))
print("Value of pi:", math.pi)
