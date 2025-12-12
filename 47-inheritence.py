class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"the name of employee: {self.id} is {self.name}")


class Programmer(Employee):     # Employee class inherited and extended
    def showLan(self):
        print("the default language is Python")


a = Employee("Ash", 34)
a.showDetails()
b = Programmer("Ash", 34)
b.showLan()