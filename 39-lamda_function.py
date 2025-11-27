# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:
# lambda arguments: expression

# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

def appl(fx, x):
    return 6 + fx(x)

# instead of writing this
# def double(x):
#     return x*2

# we can do this instead:
double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(5, 9, 7))
print(appl(cube, 2))
print(appl(lambda x: x*x*x, 2))