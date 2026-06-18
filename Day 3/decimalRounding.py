# Write a Python program to configure the rounding to round up and round down a given decimal value. Use decimal.Decimal

from decimal import Decimal, ROUND_DOWN, ROUND_UP


number = Decimal("25.6789")
round_to = Decimal("0.01")

rounded_up = number.quantize(round_to, rounding=ROUND_UP)
rounded_down = number.quantize(round_to, rounding=ROUND_DOWN)

print("Original decimal value:", number)
print("Rounded up value:", rounded_up)
print("Rounded down value:", rounded_down)
