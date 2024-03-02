PATH = "list_to_file.txt"
list = [0, 1, 2, 3, 4]

with open(PATH, 'w') as file:
    for item in list:
        file.write(str(item) + "\n")

print(f"List was successfully written into {PATH}")