class Employee:
    def __init__(self):
        self.__name = "Ash"

a = Employee()
# print(a.__name) # will throw error
print(a._Employee__name) # okay
print(a.__dir__())

class Students:
    def __init__(self):
        self._name = "Ash"

    def _funName(self):
        return "Ash-is-pilot"

class Subject(Students):
    pass

obj = Students()
obj1 = Subject()
    
print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())