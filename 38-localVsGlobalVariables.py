# A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.
# On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.

x = 4
print(x)

def hello():
    global x    # from here we define to use the global x so
    x = 5       # here we're using the global x not the local and any modifications to this will relect in the original variable x
    print(f"the local x is {x}")
    print(x)
    print("Hello Ash")

hello()
print(f"the global x is {x}")