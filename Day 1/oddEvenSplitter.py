# Covers: 
#   Lists
#   Tuples
#   Loops

# Question -> Separate the odd numbers and even numbers into two distinct lists.
# Input: A list of integers
# Output: Return a single tuple containing both lists: ([evens], [odds]).
# Ans:

# This function takes a list (array) as input, separates the numbers, and returns a tuple containing both even and odd numbers.
def oddEvenSplitter(yourList):
    evens = []
    odds = []
    for a in yourList:
        if a % 2 == 0:
            evens.append(a)
        else:
            odds.append(a)
    return ([evens], [odds])

listOfNumbers = [1, 2, 3, 4, 5, 6]
print("List:", listOfNumbers)

print("Single tuple containing both lists:", oddEvenSplitter(listOfNumbers))