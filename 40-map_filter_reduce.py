# MAP
def cube(x):
    return x**3

print(cube(4))

l = [1, 2, 4, 6, 3]
# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(cube, l))
print(newl)


# FILTER
# def filter_function(a):
#     return a>2

newl2 = list(filter(lambda x: x>2, l))
print(newl2)


# REDUCE
from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x + y, numbers)

print(sum)