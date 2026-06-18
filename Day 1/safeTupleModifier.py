# Covers: 
#   Tuples
#   Lists   
#   Casting

# Question -> Change the second item (the port) to the new port value.
# Input: A tuple ("localhost", 5432, "admin") and a new port integer (e.g., 8080)
# Output: Return the updated data back as a tuple.
# Ans: 

yourTuple = ("localhost", 5432, "admin")
print("Old Tuple:", yourTuple, ":", type(yourTuple))

yourTuple = list(yourTuple)
yourTuple[2] = 8080
yourTuple = tuple(yourTuple)

print("New Tuple:", yourTuple, ":", type(yourTuple))