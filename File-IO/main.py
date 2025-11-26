# Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.
f1 = open('myfile.txt', 'rb')   # binary (b): used to handle binary files (images, pdfs, etc).
f = open('myfile.txt', 'r')
text = f.read()     # read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
print(text)
f.close()           # It is important to close a file with close() method after you are done with it. This releases the resources used by the file and allows other programs to access it.


f2 = open('myFile2.txt', 'w')   # the write mode opens the given gile in write mode but if the file doesn't exists it will create one

# text2 = f.read()
# print(text2)
f2.close()

w = open('myFile2.txt', 'w')    # write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
w.write('Hello, this is written using the python')      # We can then use the write() method to write to the file. Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.
w.close()

# anyways there's a bit more text to open a file, read, write, and close we've a better way for it right below
with open('myFile2.txt', 'w') as f:     # with this syntax it closes the file automatically
    f.write('Hello this is written using a python code')
