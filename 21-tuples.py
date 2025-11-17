# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

tup = (1, 76, 342, 32, 4, "Ash", True)     # when creating tuple if you only add one value than it'll treat it as single value not a tuple if you want to make a tuple with single element place a comma just after the value
# tup[2] = 90     # not allowed

print(type(tup), tup)
print(tup[0])       # prints the 0th element of given tuple
print(tup[-2])      # this is the length - 2

if 342 in tup:
    print("342 is present in this tuple")

tup2 = tup[1:4]     # this will create a new tuple with the given tuple
print(tup2)