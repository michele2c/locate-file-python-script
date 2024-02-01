# Import os module
import os

# get the current working directory
cwd = os.getcwd()

# store list of dictionaries
file_dic = []

# iterate over the list of entries using in the current directory
# create the dictionary and append to the list
for file in os.listdir(cwd):
    if os.path.isfile(file): 
        file_path = os.path.join(cwd, file) 
        file_info = {
            'File': file_path,
            'Size': os.path.getsize(file_path)
        }
        file_dic.append(file_info)

print(*file_dic, sep = "\n")
