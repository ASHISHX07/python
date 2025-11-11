# we'll discuss some methods of the string
# strings are simply immutable in place meaning we cannot modify strings directly instead when we use methods on strings it creates a new copy of that string the original string remains unchanged

a = "!!!!Ashish!! !!!!!! !!Ashish"
print(len(a))
print(a)
print(a.upper()) # converts the string into the upper case
print(a.lower()) # converts the string into the lower case
print(a.rstrip("!")) # trips trailing given character
print(a.replace("Ashish", "Ash")) # replaces all string occurrences in a string with given string
print(a.split(" ")) # creates a list based on the given separator value

blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) # capitalizes the leading charater of the string and converts all other characters to small

str1 = "Welcome to the Console!!!"
print(len(str1))                # the original string was 25 characters
print(len(str1.center(50)))     # the center method added more 25 whitespaces so that sentence can move to the center

print(a.count("Ashish")) # returns how many the given string occures in the string

print (str1.endswith("!!!")) # checks if the given string ends with the given string characters

print (str1.endswith("to", 4, 10)) # checks if the given string ends with the given string characters within specified from index 4 to 10
print(str1.find("the")) # returns the first occured index of the given value if string contains or returns -1 otherwise

print(str1.index("the")) # works similar to find but if not found the given value than it throws error instead of -1

print(str1.isalnum()) # returns true if string is alpha-numeric(eg. Abcd1234) false otherwise

print(str1.isalpha()) # returns true if the given string is alphabatic(e.g. A-Z, a-z) false otherwise

print(str1.isprintable()) # returns true if all the characters in the given string is printable false otherwise

print(str1.isspace()) # returns true if the given string contains whitespaces false otherwise

print(str1.istitle()) # returns true if every word in the given string contains capital latter false otherwise

print(str1.startswith("Ashish")) # works same as ends with but for starting

print(str1.swapcase()) # swaps the uppercase to lowercase and vise versa

print(str1.title()) # makes the string capital for title