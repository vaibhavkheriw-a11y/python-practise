# Covers: 
#   Data Types 
#   Casting
#   Functions

# Question -> Convert the string to a float, apply the discount, and truncate it to a whole integer.
# Input: A price string (e.g., "19.99") and a discount float (e.g., 0.10)
# Output: Return the final whole integer.
# Ans:

# This function converts the input value to a float.
def convertStringToFloat(inputValue):
    return float(inputValue)

stringPrice = "19.99"
discount = 0.10
print("Price String: ", stringPrice, ":", type(stringPrice))
print("\nDiscount Float: ", discount, ":", type(discount))

stringPrice = convertStringToFloat("19.99")
discountedPrice = stringPrice * (1 - discount)
discountedPrice = int(discountedPrice)
print("Discounted Price Int: ", discountedPrice, ":", type(discountedPrice))