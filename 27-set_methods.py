# Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

s1 = {1, 2, 3, 5, 6}
s2 = {3, 6, 7}

print(s1.union(s2))     # A union set is a new set that combines all the unique elements from two or more sets, without repetition

# while the union() method return new set but does not change the original sets if you want to change the original sets than you can use the update() method, the update() method adds the given set values to the set without repetition
s1.update(s2)
print(s1, s2)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities.intersection(cities2))          # An intersection set is the set containing all elements that are common to two or more sets.
cities.intersection_update(cities2)   # the intersection_update() method updates the set with given set by putting all the common items in the set and discarding all uncommon items
print(cities, cities2)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

l = cities.symmetric_difference(cities2)     # The symmetric difference of two sets is the set of elements that are in either of the sets, but not in their intersection and order doesn't matter
print(l)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = {"Seoul", "Madrid", "Kabul"}

print(cities.isdisjoint(cities2))       # The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

print(cities2.issuperset(cities3))       # The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

print(cities3.issubset(cities2))      # The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

cities.add("Helsinki")
print(cities)       # If you want to add a single item to the set use the add() method.

cities.remove("Helsinki")   # We can use remove() and discard() methods to remove items form list. The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()     # The pop() method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
print(cities)
print(item)

# del cities        # # del is not a method, rather it is a keyword which deletes the set entirely.
# print(cities)

cities.clear()      # This method clears all items in the set and prints an empty set.
print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")