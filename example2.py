def welcome():
    print("Hey you're welcome from ash")

print(__name__)     # the name is the property which tells us from where the function call is made
if __name__ == "__main__":      # with this conditional we can prevent the  double call problem when called from other file as if the __name__ is called from __main__ which is the main module or the origin of the function which is this file than execute this function otherwise don't and the function will execute in the file that called
    welcome()       # the function is called in file itself