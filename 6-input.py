a = input("Enter your name: ") # the input asks the user to input something like number, text etc. and prints the corresponding string to the console and store the input value to the variable 
print("my name is", a)

x = input("Enter first number: ")
y = input("Enter first number: ")
# print(x + y) # this will not result as addition of the entered number as the input always stores in string
print(int(x) + int(y)) # thus will result in addition because now we converted to integer
