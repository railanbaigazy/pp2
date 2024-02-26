import re

def camel_to_snake(match):
    group = match.group(0)
    snake_case = group[0] + '_' + group[1].lower()
    return snake_case

content = "camelCase"

# with open('row.txt', 'r') as file:
#     content = file.read()

snake_cased = re.sub(r'[a-z][A-Z]', camel_to_snake, content)

print(snake_cased)