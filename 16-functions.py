def calculateGmean(a, b):       # def function_name(parameters): function body with a indent on next line
    mean = (a * b) / (a + b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print(a, "is greater than", b)
    else:
        print(a, "is less than or equal to", b)

def isLesser(a, b):
    pass        # pass keyword is used to pass to the next statement as we intend to write the function body later

calculateGmean(7, 8)
calculateGmean(9, 8)
isGreater(7, 9)
isGreater(3544, 2654)