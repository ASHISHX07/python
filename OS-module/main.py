import os       # imports the os module
if(not os.path.exists("data")):     # if there's no data directory
    os.mkdir("data")                # then create the folder data

for i in range(10):
    os.mkdir(f"data/day{i+1}")      # we looped to create 10 files with a loop
    