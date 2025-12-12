class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"value is {self._value}")

    @property                       # getter
    def value(self):
        return 10 * self._value
    
    @value.setter                   # setter
    def valuen(self, val):
        self._value = val/10
    

obj = MyClass(10)
obj.valuen = 67
print(obj.value)
obj.show()