import os
import time
import sys
import shutil
import helper

# Adding better logging for myself, command lind is not cutting it.
old_stdout = sys.stdout
log_file = open("output.log", "w")
sys.stdout = log_file

# getting all the files - All files
dirname = "/Users/mattweiss/Desktop/"
files = os.listdir(dirname)
doc_home = "/Users/mattweiss/Documents"
pic_home = "/Users/mattweiss/Pictures"
code_home = "/Users/mattweiss/Code"
movie_home = "/Users/mattweiss/Movies"


now = time.time()

for file in files:
    # Getting file extention for sorting
    split_tup = os.path.splitext(file)
    file_extension = split_tup[1]

    # Path to the file/directory
    path = f"{dirname}{file}"
    days = helper.daysSinceLastUpdated(path)

    if days > 1:
        if file_extension == '.pdf' or file_extension == ".txt" or file_extension == '.mobi' or file_extension == '.csv' or file_extension == '.xlsx' or file_extension == '.docx' or file_extension == '.html':
            dest = shutil.move(path, doc_home)
            print(f"Moving! {path} to {doc_home}")
        elif file_extension == '.png' or file_extension == '.jpg' or file_extension == '.jpeg':
            dest = shutil.move(path, pic_home)
            print(f"Moving! {path} to {pic_home}")
        elif file_extension == '.dmg' or file_extension == '.pkg':
            dest = shutil.move(path, code_home)
            print(f"Moving! {path} to {code_home}")
        elif file_extension == '.mov':
            dest = shutil.move(path, movie_home)
            print(f"Moving! {path} to {movie_home}")
        else:
            print(
                f"ACTION REQUIRED: We did not move {path}: File Type: {file_extension}")
