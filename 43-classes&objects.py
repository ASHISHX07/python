class person:
    name = "Ash"
    occupation = "salaried"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()

a.name = "Ash"
a.occupation = "unemployed"

b.name = "Ashish"
b.occupation = "trader"

a.info()
b.info()