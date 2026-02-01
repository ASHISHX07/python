class Employee:
    companyName = "Apple"
    def __init__(self, name):
        self.name = name
        self.raiseAmount = 0.02
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amout in {self.companyName} is {self.raiseAmount}")

emp1 = Employee("harry")
emp1.raiseAmount = 0.03
emp1.showDetails()
emp2 = Employee("rohan")
emp2.showDetails()

# Employee.showDetails(emp1)