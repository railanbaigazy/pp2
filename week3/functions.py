# Write a function called calculate_factorial that takes a positive integer as a parameter and returns its factorial (use recursion)

def calculate_factorial(num):
    if num == 0:
        return 1
    return num * calculate_factorial(num-1)


# Write a function called reverse_string that takes a string as a parameter and returns its reverse.

def reverse_string(str):
    # reversed_string = ""
    # for i in range(len(str) - 1, -1, -1):
    #     reversed_string += str[i]
    # return reversed_string
    return str[::-1]

# Write a function called get_max that takes three parameters (a, b, and c) and returns the maximum of the three.

def get_max(a, b, c):
    # max = a
    # if b > max:
    #     max = b
    # if c > max:
    #     max = c
    # return max
    return max(a, b, c)
    
# Write a function called is_even that takes an integer as a parameter and returns True if it's even and False otherwise.

def is_even(num):
    return num % 2 == 0

# You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an argument and returns only prime numbers from the list.

numbers = "1 2 3 4 5 6 7 8 9"
nums_list = [int(x) for x in numbers.split()]

def filter_prime(nums):
    prime_nums = []
    for num in nums:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0: 
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    return prime_nums

print(filter_prime(nums_list))

# Write a function find_common_elements that takes two lists as parameters and returns a new list containing common elements between them.

def find_common_elements(list_a, list_b):
    common_list = []
    for el in list_a:
        if el in list_b:
            common_list.append(el)
    return common_list

# Write a function word_frequency that takes a string as input and returns a dictionary where keys are unique words, and values are their frequencies.

def word_frequency(string):
    words_list = string.split()
    words_dict = {}

    for word in words_list:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    return words_dict
print(word_frequency("hi hi my name is my name is Railan"))

# Write a recursive function fibonacci that returns the nth Fibonacci number.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Write a function calculate_running_average that takes a series of numbers as input and returns a list containing the running average at each position.

def calculate_running_average(nums):
    averages = [nums[0]]
    for i in range(1, len(nums)):
        sum = 0
        for j in range(i + 1):
            sum += nums[j]
        averages.append(sum/(i + 1))
    return averages

print(calculate_running_average([1, 2, 3, 4]))