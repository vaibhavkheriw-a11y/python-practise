# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Write a Python program to remove all duplicate elements from a given array and returns a new array.

def uniqueElementsOfList(inputList):
    elementCount = 0
    outputList = []
    for a in inputList:
        for b in inputList:
            if a == b:
                if elementCount == 0:
                    elementCount += 1
                elif elementCount == 1:
                    elementCount = 0
                    break
        if elementCount == 1:
            outputList.append(a)
    return outputList

myList = ['s', 'f', 's', 'g', 'h', 'i', 'h', 'a']
print(f"My list: {myList}. Unique elements in this list are {uniqueElementsOfList(myList)}")