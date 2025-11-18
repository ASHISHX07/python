# PYTHON SETS
# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

s = {2, 4, 2, 6}    # all the duplicate values in a set will be discarded so one element of 2 will be discarded
print(s)

info = {"Ash", 20, False, 5.5}
print(info)

# a = {}        # this will create an empty dictionary not a set
a = set()       # to create an empty set use the set() method 
print(type(a)) 

for value in info:      # sets can be used with loops
    print(value)