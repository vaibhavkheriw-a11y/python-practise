# Array

myArrayStr = ['v', 'a', 'i', 'b', 'h', 'a', 'v']
myArrayNum = [0, 2, 4, 3, 4, 56, 64, 32412, 3, 0, 0, 0, 73]

print(f"My array = {myArrayStr}")
print(f"My number array = {myArrayNum}")
print(f"My array size = {len(myArrayStr)}")

myArrayStr.sort()
print(f"My array sort = {myArrayStr}")

myArrayNum.sort()
print(f"My number array sort = {myArrayNum}")

print(f"My array count 'v' = {myArrayStr.count('v')}")
print(f"My number array count 0 = {myArrayNum.count(0)}")
print(f"My array index of 'i' = {myArrayStr.index('i')}")

myArrayNum.reverse()
print(f"Reverse my number array = {myArrayNum}")

myArrayStr.reverse()
print(f"Reverse my array = {myArrayStr}")

myArrayStr.append("kheriwal")
print(f"Append in my array = {myArrayStr}")

myArrayNum.append(5)
print(f"Append in my number array = {myArrayNum}")
 
myArrayStr.insert(0, 'Hello')
print(f"Insert in my array = {myArrayStr}")

myArrayNum.remove(0)
print(f"Remove 0 from my number array = {myArrayNum}")

myArrayStr.pop(1)
print(f"Pop at 1st index in my array = {myArrayStr}")

myArrayStr.clear()
print(f"Clear my array = {myArrayStr}")

myArrayNum.sort(reverse=True)
print(f"My number array sort = {myArrayNum}")