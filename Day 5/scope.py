name = "Riya" # Global Scope

def localScope():
    name = "Vaibhav" # Local Scope
    print(name)

def globalScope():
    global name
    print(name)
    name = "Vaibhav Riya" # Global Scope
    print(name)

def enclosingScope():
    name = "I love GTA"
    print(name)

    def innerEnclosingScope():
        nonlocal name 
        name = "I love GTA VI"
        print(name)
    
    innerEnclosingScope()

localScope()
globalScope()
enclosingScope()