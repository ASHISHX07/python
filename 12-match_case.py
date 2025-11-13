x = int(input("Enter the value for x: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if x != 90:
        print(x, " is not 90")
    case _ if x != 80:
        print(x, " is not 80")
    case _:     # underscore '_' is used to define default case
        print(x)