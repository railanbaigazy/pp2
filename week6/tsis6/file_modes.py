import os

PATH = "../../"

def check_access(path):
    info = {}
    info["exists"] = os.path.exists(path)

    if info["exists"]:
        info["read"] = os.access(path, os.R_OK)
        info["write"] = os.access(path, os.W_OK)
        info["execute"] = os.access(path, os.X_OK)
    else:
        info["read"] = False
        info["write"] = False
        info["execute"] = False
    
    return info

access_info = check_access(PATH)

print(f"Path: {PATH}\nAccess information:\n{access_info}")