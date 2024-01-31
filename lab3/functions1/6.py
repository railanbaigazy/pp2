#6. Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

input = input("Input string: ")

def reverse_sentence(input):
    input_list = input.split()
    reversed_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return " ".join(reversed_list)

print(reverse_sentence(input))