marks = [12, 56, 32, 98, 12, 45, 1, 4]


# instead of doing this
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("Ash awesome!")
    index += 1
    

# we can do this
for index, mark in enumerate(marks, start=1):    # we add the enumerate() method in which we pass iterable object like list, and then we can access the index and value note that index, mark is just names we can use any names for it but order matters where is we use just one value instead of two (index, mark) we gets the tuple but with using two values (index, mark) we gets the unpacked tuple, we can optionally pass a start=<value> which gives a starting point of the given iterable Object by default it goes from 0 index as we all when but when given start it'll start with 1, 2, 3, .... note that it'll still iterate through all the elements the start is just a number from which to start count 
    print(mark)
    if(index == 3):
        print("Ash awesome!")