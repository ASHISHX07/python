# Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

# To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:

import math                         # imported math module
from math import sqrt, pi           # with from and import keyword we can import methods needed
from math import *                  # with * mark all the methods are imported
from math import sqrt as s          # we can also import sqrt from math as s
import math as m                    # here we're importing math as m
from example import welcome, Ash    # here we imported our own custom py file containing the Ash object and welcome method

# math.floor(4.2343)

# result = math.sqrt(9)             # not needed when you imported the methods individually 
result = sqrt(9) * pi
print(result)

print(dir(math))                    # with dir() method we can access the functions and methods the dir is coming when imported

welcome()                           # imported from our own python file
print(Ash)                          # imported from out own python file