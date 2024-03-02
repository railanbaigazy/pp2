for i in range(26):
    filename = f"{chr(ord('A') + i)}.txt"
    with open(filename, "w") as file:
        file.write("")
    print(f"File {filename} was generated")

print("All files from A to Z were generated successfully!")