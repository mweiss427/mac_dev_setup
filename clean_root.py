import os
import re
import time
import sys
import shutil
import helper

# Adding better logging for myself, command lind is not cutting it.
old_stdout = sys.stdout
log_file = open("output.log", "w")
sys.stdout = log_file

# getting all the files - All files
dirname = '../'
files = os.listdir(dirname)
regex = re.compile('^[a-z]')
filteredFiles = [i for i in files if regex.match(i)]
code_grave_yard = "/Users/mattweiss/Code"
now = time.time()

for file in filteredFiles:
    # Path to the file/directory
    path = f"{dirname}{file}"
    days = helper.daysSinceLastUpdated(path)

    if days > 30:
        dest = shutil.move(path, code_grave_yard)
        print(f"Moving! {path} to the grave yard!")
