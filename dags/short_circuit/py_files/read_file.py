import json


def read_json(path):
    with open(path, 'r') as f:
        data = json.load(f)

    print(data)
    print("Name:", data.get("name"))
    print("Hobbies:", data.get("hobbies"))