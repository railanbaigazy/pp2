import re

with open('row.txt', 'r') as file:
    content = file.read()

match = re.sub('[ ,.]', ':', content)
print(match)