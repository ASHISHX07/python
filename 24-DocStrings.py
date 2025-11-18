# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

def square(n):
    # print(n)        # not allowed if you do this than the the string below not considered docstring
    '''Takes in a number n, returns the square of n'''      # this is docstring which tells us about the function
    print(n**2)

square(5)
print(square.__doc__)       # the __doc__ attribute prints the actual docstring 

# PYTHON COMMENTS VS DOCSTRINGS

# Python Comments
# Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

# Python docstrings
# As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

# We can access these docstrings using the __doc__ attribute.

# PEP 8

# PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

# PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.