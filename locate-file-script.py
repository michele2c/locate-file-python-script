import os
import json

def human_readable_size(size):
    # Convert size to human-readable format
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0

def locate_file(cwd=None):
    if cwd is None: # Default to the current working directory if path is not provided
        cwd = os.getcwd()
    file_dic = []  # List to store dictionaries about files

    # Walk through the directory and subdirectories
    # underscore(_), to indicate that the loop variable "subfolders" is intentionally not being used in the loop body
    for folder, _, files in os.walk(cwd):
        for file in files:
            # Skip hidden files (starting with .)
            if file.startswith('.'):
                continue
            
            file_path = os.path.join(folder, file)
            file_info = {
                'File': file_path,
                'Size': human_readable_size(os.path.getsize(file_path))
                }
            file_dic.append(file_info) # append the file_info to file_dic

    return file_dic # return the list of dictionary

# Usage
if __name__ == "__main__":

    user_input = input("Enter the path: ")
    if not user_input:
        user_input = None

    response = locate_file(user_input)
    for file_info in response:
        print(json.dumps(file_info, indent=1))
