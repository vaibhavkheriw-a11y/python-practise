# Write a Python program to display a given decimal value in scientific notation. Use decimal.Decimal

from decimal import Decimal


number = Decimal("123456.789")

print("Decimal value:", number)
print("Scientific notation:", "{:E}".format(number))
