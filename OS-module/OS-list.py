import os

folders = os.listdir("data")    # the listdir("<DIR_NAME>") returns a list of the file/folder inside the given DIR

print(folders)

for folder in folders:          # we can loop through each folder in a list of files/folders further we can create folders in the given folder
    print(folder)
    print(os.listdir(f"data/{folder}"))   # prints files and folders inside the given folder for the whole folder

print(dir(os))
print(os.getcwd())      # the getcwd() returns current working directory
os.chdir("C:/Users")    # the chdird("<PATH_TO_DIR>") method changes the current working directory to the given directory
print(os.getcwd())