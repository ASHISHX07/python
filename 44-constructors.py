class Person:
    def __init__(self, n, o):       # the __init__ is constructor function
        print("Hey I'm a person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Ash", "unelmployed")
b = Person("Ashish", "Trader")
a.info()
b.info()
# a.name = "Ashish"
# a.occ = "trader"

# a.info()