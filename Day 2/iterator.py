# Iterator

def iterator(obj):
    i = 0
    objList = []
    objIterator = iter(obj)
    while i < len(obj):
        objList.append(next(objIterator))
        i += 1
    return objList

print(iterator("GTASA"))