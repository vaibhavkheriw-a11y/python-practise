# Covers: 
#   Tuples
#   Lists   
#   Loops

# Question -> Find the lowestest and highestest numbers using a for loop
# Input: A list of numbers
# Output: Return a tuple: (lowestest, highestest).
# Ans: 

numbers = [1, 432, 43, 75, 13, 78]
print("List of numbers: ", numbers)

def trackingExtremes(listOfNum):
    lowest = numbers[0]
    highest = numbers[0]
    for a in listOfNum:
        if a < lowest:
            lowest = a
        elif a > highest:
            highest = a
    return lowest, highest

print("Lowestest and highestest in list", trackingExtremes(numbers))