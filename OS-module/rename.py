import os       # imports the os module

for i in range(10):
    os.rename(f"data/day{i+1}", f"data/day-{i+1}")      # we looped to rename all the folders the first argument is for the DIR name we want to rename and the second argument is the new name
    