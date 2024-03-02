buffer = ""

with open("input.txt", "r") as file:
    buffer = file.read()

print("Contents of input were copied into buffer")

with open("output.txt", "w") as file:
    file.write(buffer)

print("Successfully pasted the content")