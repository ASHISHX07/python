# Tuples are immutable. hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. then perform operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")

print(countries)

temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[1] = "Finland"

countries = tuple(temp)

print(countries)

countries2 = ("Pakistan", "Afghanistan", "Bangladesh", "Sri-Lanka")
newCountries = ("Vietnam", "India", "China")
southEastAsia = countries2 + newCountries       # concatinates the tuples
print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)       # returns the count of the given value in the tuple
res1 = tuple1.index(3)       # returns the index of first occurence of the given value in the tuple if you want further you can also give it a range
print("Count of 3 in tuple1 is:", res)
print("index of 3 in tuple1 is:", res1)