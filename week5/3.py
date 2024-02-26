import re

with open('row.txt', 'r') as file:
    content = file.read()

match = re.findall(r'[a-z]+_[a-z]+', content)
print(match)