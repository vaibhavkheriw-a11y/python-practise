# Write a Python program to shuffle the elements of a given list. Use random.shuffle()

import random

numbers = [10, 20, 30, 40, 50]
print("List - ", numbers)
random.shuffle(numbers)
print("Shuffled list - ", numbers)