# In python, anything that you enclose between single or double quotation marks is considered a string, A string is essentially a sequence of textual data. Strings are used when working with Unicode characters.
name = "Ashish"
surname = 'Sindhav'
apple = 'He said, "I want to eat an apple"'

apple2 = '''He said,
"I want to eat an apple"''' # the tripple single or double quotes (eg. '''''' or """""" than this allows to write string on multiple lines and will be stored and printed as it is)
print("Hello, " + name)
# print(apple)
print(apple2)

print(name[0]) # we can access a character in a string by applying a [index] here at 0th position in name there's A character 
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6]) # this will throw index error as there's nothing in index 6 in the name string

for i in apple2:
    print(i)