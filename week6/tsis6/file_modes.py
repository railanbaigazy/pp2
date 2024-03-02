import os

PATH = input("Input your path: ")

def check_access(path):
    info = {}
    if not os.path.exists(path):
        raise FileNotFoundError("No such path exists")

    info["read"] = os.access(path, os.R_OK)
    info["write"] = os.access(path, os.W_OK)
    info["execute"] = os.access(path, os.X_OK)

    return info

try:
    access_info = check_access(PATH)
    print(f"Path: {PATH}\nAccess information:\n{access_info}")
except FileNotFoundError as e:
    print(e)
