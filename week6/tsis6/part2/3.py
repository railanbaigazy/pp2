# Write a Python program with built-in function that checks whether a passed string is palindrome or not.

text = input("Your text: ")

is_palindrome = True if text[::-1] == text else False

print(f'Text "{text}" is{"" if is_palindrome else " not"} a palindrome')