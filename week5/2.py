import re

with open('row.txt', 'r') as file:
    content = file.read()

match = re.search(r'ab{2,3}', content)
print(match)