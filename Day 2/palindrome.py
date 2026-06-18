# Write a Python function that checks whether a passed string is palindrome or not.

def palindrome(inputString):
    i = len(inputString)
    for a in inputString:
        i -= 1
        if i == int(len(inputString)/2 - 1):
            return "String is palindrome."
        if a != inputString[i]:
            return "String is not palindrome."

print(palindrome("Vaibhav"))