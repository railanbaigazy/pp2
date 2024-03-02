# Write a Python program with built-in function that accepts a string and calculate the number of upper case letters and lowercase letters

input_text = input("Your text: ")

upper_count = sum(1 for ch in input_text if ch.isupper())
lower_count = sum(1 for ch in input_text if ch.islower())

print(f"Upper count: {upper_count}")
print(f"Lower count: {lower_count}")