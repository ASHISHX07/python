# string slicing is operations that is performed on a string to modify, replace strings

name = "Ashish,Kinjal"

print(name[0:6]) # when we do this it gives us the characters from 0 to 5 in the name string
print(len(name)) # the len() method gives us the length of the given string but it gives the length which is not index as index always starts with 0 index will be always length-1

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
print(fruit[0:4])
print(fruit[:4])
print(fruit[:])
print(fruit[0:-3]) # the negative slicing works same as len(fruit)-3 which is 2 so it prints from 0 to 2 which is Ma
print(fruit[0:len(fruit)-3]) # same as just before
print(fruit[-1:-3]) # this doesn't makes any sense because 5-1=4 and 5-3=2 which doesn't gives valid index to print
print(fruit[-3:-1]) # this makes sense because 5-3=2 and 5-1=4 which is 2:4 which is ng

# nm = "Harry"
# print(nm[-4:-2])