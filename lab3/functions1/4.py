#4. You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

input_list = input("Input list with numbers separated separated by spaces: ").split()

def filter_prime(list):
    for num in list:
        num = int(num)
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if (is_prime):
            print(num)

filter_prime(input_list)