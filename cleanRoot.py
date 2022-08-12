import os
import re
import time
import sys
import shutil

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

print(f"the current time is: {now}")

for file in filteredFiles:
    # Path to the file/directory
    path = f"../{file}"

    # Both the variables would contain time
    # elapsed since EPOCH in float
    time_created = os.path.getctime(path)
    time_last_changed = os.path.getmtime(path)

    # Get the difference between now and when the time was last modified.
    elapsed_time = now - time_last_changed

    # Converting the time in seconds to a timestamp for printing
    c_ti = time.ctime(time_created)
    days = 0
    if elapsed_time >= 86400:
        days = int(elapsed_time / 86400)
    elapsed = time.strftime(
        "%H:%M:%S", time.gmtime(time.time() - time_created))
    m_ti = time.ctime(elapsed_time)

    print(
        f"File: {path} - Created: {c_ti} - Last Modified {days} days ago")

    if days > 30:
        dest = shutil.move(path, code_grave_yard)
        print(f"Moving! {path} to the grave yard!")
