import json

with open("api/data1.json", "r") as file:
    data1 = json.load(file)

print(data1)
print(type(data1))