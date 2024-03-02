# Write a Python program that invoke square root function after specific milliseconds​
# Sample Input:​
# 25100​
# 2123​
# Sample Output:​
# Square root of 25100 after 2123 miliseconds is 158.42979517754858​

import time, math

num = int(input())
ms = int(input())

time.sleep(ms / 1000)
root = math.sqrt(num)
print(f"Square root of {num} after {ms} milliseconds is {root}")