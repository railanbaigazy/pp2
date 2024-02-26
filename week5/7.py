import re

def snake_to_camel(match):
    snake_case = match.group(0)
    camel_case = snake_case[0] + snake_case[1:3].replace('_', '').capitalize()
    return camel_case


with open('row.txt', 'r') as file:
    content = file.read()

camel_case = re.sub(r'[a-zA-Z]_[a-zA-Z]', snake_to_camel, content)
print(camel_case)