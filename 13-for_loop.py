# loops are used when we wants to execute some code repeatedly until some condition is met

name = "Ashish"

# for i in name:
#     print(i, end=", ")
#     if(i == "h"):
#         print("h came", end=", ")

colors = ["Red", "Green", "Blue", "Yellow"]     # this is list ignore it for now

# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

for k in range(5):      # range method iterates until given value
    print(k+1)

for k in range(1, 11):   # prints from 1 to 8
    print(k)

for k in range(0, 11, 2): # here the parameters are start, stop, step
    print(k)