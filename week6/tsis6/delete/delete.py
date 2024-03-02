import os

PATH = input("Give a path of the file to delete: ")

try:
    os.remove(PATH)
    print("Successfully removed")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You have no permission to remove it")
except Exception as e:
    print(e)