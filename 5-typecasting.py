a = "1"
b = "2"
# print(a + b) # this will print 12 instead of 3 beacuse both a and b is string not a number, integer or float
print(int(a) + int(b)) # the int() method converts the given value of variable to the type int but the origin value must be covertible like 1 and 2 in a and b is number but if you try to do the same with "Apple" so this is not valid
print(str(a) + str(b)) # another example of type conversion

# implicit typecasting

c = 1.9
d = 8
print(c + d) # this will convert the d variable to float, as python implicitly converts the smaller datatype to the higher one 