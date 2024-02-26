import re

with open('row.txt', 'r') as file:
    content = file.read()

x = re.search(r'a+b*', content)
print(x)