import re

def spacing(match):
    group = match.group(0)
    return group[0] + " " + group[1]

content = "HelloMyNameIsRailan"

# with open('row.txt', 'r') as file:
#     content = file.read()

title_with_spaces = re.sub(r'.[A-Z]', spacing, content)
print(title_with_spaces)