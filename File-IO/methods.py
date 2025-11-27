# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.
f = open('myFile3.txt', 'r')
while True:
    line = f .readline()
    if not line:
        break
    print(line)

# The readlines() method reads all the lines of the file and returns them as a list of strings.

f2 = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f2.write(line + '\n')
f2.close()


# # Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:
f3 = open('myfile1.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f3.writelines(lines)
f3.close()