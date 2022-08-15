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
dirname = '/Users/mattweiss/Code/'
files = os.listdir(dirname)
regex = re.compile('^[a-z]')
filteredFiles = [i for i in files if regex.match(i)]
now = time.time()

for file in filteredFiles:
    # Path to the file/directory
    path = f"{dirname}{file}"
    days = helper.daysSinceLastUpdated(path)

    if days > 30:
        print(
            f"Removing {path} from device! Its been untouched for {days} days")
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)
