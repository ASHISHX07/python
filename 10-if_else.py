# a = int(input("Enter your age: "))
# print("Your age is:", a)

# # conditional operators
# # >, <, >=, <=, ==, !=

# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# # an if keyword takes a conditional statement if true than it executes the following code block and if false than execute the false block also all the statement written after colon with a indent is considered to be part of the repective condition
# if (a > 18):
#     print("You can drive")
# else:
#     print("You cannot drive")

# applePrice = 10
# budget = 200
# if (budget - applePrice > 50):
#     print("Alexa, add 1kg Apples to the cart.")
# else:
#     print("Alexa, do not add apples to the cart.")

num = int(input("Enter the value of num: "))
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
elif (num == 999):
    print("Special number")
else:
    print("Number is positive.")