# Covers: 
#   If-Else
#   Data Types
#   Functions

# Question -> Determine ticket price based on these rules:
#   Age under 5 - Price is 0
#   Age 5 to 18 OR student - Price is 10
#   Everyone else - Price is 20
# Input: An age integer and a student boolean (True/False)
# Output: Return the price integer.
# Ans:

# This will check the age and student status and give you the ticket price accordingly.
def ticketGate(age,isStudent):
    if age < 5:
        return 0
    elif (age >= 5 and age <= 18) or isStudent == True:
        return 10
    else:
        return 20
    
age = 20
print("For age:", age, "\nTicket Price:", ticketGate(age, True))
