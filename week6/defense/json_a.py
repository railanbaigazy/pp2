import json

some_json = '{"name": "Railan", "age": "19", "grade": "1", "university_name": "KBTU"}'

data = json.loads(some_json)

print(f"Name: {data["name"]}")

with open("data.json", "w") as file:
    json_str = json.dumps(data)
    file.write(json_str)