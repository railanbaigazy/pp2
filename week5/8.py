import re

content = "ahskjfhasjfFfsafhsaLfhSgsagsaGh"

# with open('row.txt', 'r') as file:
#     content = file.read()

match = re.split(r'[A-Z]', content)

print(match)