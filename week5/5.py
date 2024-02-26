import re

with open('row.txt', 'r') as file:
    content = file.read()

match = re.search(r'a.*b', content)
print(match)