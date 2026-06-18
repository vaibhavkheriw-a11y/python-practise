# variable and function naming convention 
# snake_case

user_name = "Vaibhav Kheriwal"
my_number = 100
is_work = True

def get_my_details():
    print(f"Name : {user_name}, Number: {my_number}, Work: {is_work}")

get_my_details()

# class naming convention 
# PascalCase

class MyWork:

    # class variable
    # belongs to the class and is shared by all objects.
    public_name = "Vaibhav"
    _protected_name = "Kheriwal"
    __private_name = "Riya"

    def show_private_name(self):
        return MyWork.__private_name
    
    def __init__(self):
        # object variable, all variables must be created here before using them.
        # belong to each object created from the class.
        self.age = 0
        self._data = "GTA"
        self.__color = "Red"

    def get_color(self):
        return self.__color

print(MyWork.public_name)
print(MyWork._protected_name)

obj = MyWork()

print(obj.public_name)
print(obj._protected_name)
print(obj.show_private_name())

print(obj.age)
print(obj._data)
print(obj.get_color())