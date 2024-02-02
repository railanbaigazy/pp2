from itertools import permutations
#5. Write a function that accepts string from user and print all permutations of that string.

input = input("Input string: ")

def string_permutations(str):
    permutation_list = permutations(str)
    for permutation in permutation_list:
        print("".join(permutation))

string_permutations(input)