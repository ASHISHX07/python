# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.
# Lists are iterable meaning we can use it with loops
# Lists can multiple types of data

l = [3, 5, 6]

print(l)
print(type(l))

marks = [3, 5, 6, "Ash", True, 6, 7, 54, 12]

print(marks[1]) # prints the 1st index element of the list
print(marks[-3]) # ---------------\
print(marks[len(marks)-3]) # ------} all three prints same
print(marks[2]) #-----------------/

if "Ash" in marks: # the in keyword checks if the left operand of in (7) is present in the right operand of the in (marks) returns true if it contains or false otherwise 
    print("yes")
else:
    print("no")

if "sh" in "Ash": # same applies for strings and this will print yes as string "Ash" contains "sh"
    print("Yes")
else:
    print("no")

print(marks)
print(marks[:]) # treated like 0:len(marks) implicitly
print(marks[1:-1])
print(marks[1:])
print(marks[1:4:2])

# LIST COMPREHENSION
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

lst = [i*i for i in range(4)] # we can give a statement that will be evaluated to create the list element as the iterable (loop) runs (i*i) here.
print(lst)

lst1 = [i*i for i in range(4) if i%2==0] # the condition here (if i%2==0) checks and will only include the current iterated element if the condition evaluates to true if false than that element will be excluded from the list
print(lst1)