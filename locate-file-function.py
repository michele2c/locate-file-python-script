import os

# define the function
def locate_file(cwd=None):
    if cwd is None:
        cwd = os.getcwd()
    file_dic = []  
    # Walk through the directory and subdirectories
    # get get path + file and create the dictionary
    for folder, _, files in os.walk(cwd):
        for file in files:
            file_path = os.path.join(folder, file)
            file_info = {
                'File': file_path,
                'Size': os.path.getsize(file_path)
                }
            file_dic.append(file_info)
# return the list of dictionary
    return file_dic

# Example
response = locate_file("/your/path/goes/here/")
print(*response, sep="\n")