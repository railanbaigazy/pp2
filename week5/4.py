import re

with open('row.txt', 'r') as file:
    content = file.read()

match = re.findall(r'[A-Z][a-z]+', content)
print(match)