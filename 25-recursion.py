# Recursion is the process of defining something in terms of itself.
# Python Recursive Function
# In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)   # here we're calling the factorial function inside the factorial function itself and this works fine

print(factorial(5))

# explaination:
# we called the function factorial() with argument 5
# then execution is not eligible for if block so it'll go to the else block
# then else returns n * factorial(n-1) this line is slightly complex
# here n is straight forward but then it is multiplied with factorial(n-1)
# here the call to factorial(n-1) which is 4 is called which again goes to false and again it calls 2 and so on.
# like this:    
#           5 * factorial(4)
#           5 * 4 * factorial(3)
#           5 * 4 * 3 * factorial(2)
#           5 * 4 * 3 * 2 * factorial(1)
# but this is quite difficult to understand is better made with loop