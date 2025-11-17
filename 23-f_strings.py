letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Ash"

print(letter.format(name, country))    # this will put the name at the first place in the string where {curly_braces} occured first time and country to the second occurence of {curly_braces} (Here order matters) we can also do it simple by proving the number in the curly braces for the order index but this is hard to understand and we've more code to write instead we've better approach called f-strings

print(f"Hey my name is {name} and I am from {country}")     # we add a f prefix before double quotes and than inject the variable directly inside the {curly_braces}
print(f"We can print f-strings like this: Hey my name is {{name}} and I am from {country}")     # to print the {name} as it is instead of variables in the place we can use double pairs of curly braces



txt = "For only {price:.2f} dollars!"       # the .2f suffix will store the precision of 2 decimal therefore the price 49.0999999 will be stored as 49.10
print(txt.format(price = 49.0999999))


price = 49.0999999
txt = f"For only {price:.2f} dollars!"      # this is the same example as above but with f-string
print(txt)



print(f"{2 * 30}")      # we can use a expression in the f strings but this is good for small expressions like this one for longer one's use variables instead