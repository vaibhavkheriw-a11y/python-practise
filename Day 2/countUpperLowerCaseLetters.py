# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def countUpperLowerCaseLetters(inputString=""):
    upper = 0
    lower = 0
    for a in inputString:
        if a.isupper():
            upper += 1
        elif a.islower():
            lower += 1
    return f"Upper: {upper} : Lower: {lower}"

myName = "Vaibhav Kheriwal"
print(f"My name is {myName}\n{countUpperLowerCaseLetters(myName)}")