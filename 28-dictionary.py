# Dictionaries are ordered collection (Python 3.7 onwards) of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {} much like JS objects.

dict = {
    "Ash": "Human Being",
    "Spoon": "Object"
}

print(dict["Ash"])      # "Ash" is the key in which the "Human Being" value is assigned we can access the value with it's key

emp = {
    344: "Ashish",
    56: "Shubham",
    678: "Zakir",
    567: "Neha"
}

print(emp[344])

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])     # will throw error if unavailable
print(info.get('name')) # will not throw error if unavailable
print(info.values())    # We can print all the values in the dictionary using values() method.
print(info.keys())    # We can print all the keys in the dictionary using keys() method.

for key in info.keys(): # we can also iterate through dictionary keys
    print(f"the value corresponding to {key} is {info[key]}")

print(info.items())     # the items() returns a tuple of key: value pairs of dictionary

for key, value in info.items():
    print(f"the value corresponding to the key {key} is {value}")