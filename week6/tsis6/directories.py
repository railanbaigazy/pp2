import os 

PATH = "../../"

def list_dirs(path):
    directories = []

    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            directories.append(dir)

    return directories

def list_files(path):
    files = []

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)

    return files

def list_all(path):
    dirs_and_files = os.listdir(path)
    return dirs_and_files


response = input("Choose which list do you want: d / f / all: ")

if response == "d":
    print(f"Directories:\n {list_dirs(PATH)}")
elif response == "f":
    print(f"Files:\n {list_files(PATH)}")
elif response == "all":
    print(f"Directories and Files:\n {list_all(PATH)}")
else:
    print("No such command")
