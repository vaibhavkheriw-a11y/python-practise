# Write a Python program to find the missing number in a given array of numbers between 10 and 20.

def findMissingNumber(fromNum = 0, toNum = 0, inputList = []):
    outputList = []
    while fromNum <= toNum:
        if fromNum not in inputList:
            outputList.append(fromNum)
        fromNum += 1
    return outputList

numbers = [10, 11, 13, 14, 16, 18, 19]
print(findMissingNumber(10, 20, numbers))
