# def average(a, b, c=1):
#     print("The average is ", (a+b+c)/3)

# average(a=1, b=9)

def average(*numbers):      # *numbers gives a tuple with any number of arguments given
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

# def name(fname, mname = "Ashish", lname = "Sindhav"):
#     print("Hello,", fname, mname, lname)

# name()

# average(a=21) # with this sytax the order of the parameters doesn't matter as each argument will assign to respective value

c = average(4,6,8,10)
print(c)

def name(**name):       # **name gives a dictionary with any number of key value pairs given
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")