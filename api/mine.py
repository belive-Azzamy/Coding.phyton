import json

# python - Json
data = {
    "employees" : [
        {
            "name" : "Jhon",
            "age" : 26
        },
        {
            "name" : "Mark",
            "age" : 30
        },
        {
            "name" : "Josh",
            "age" : 28
        }
    ],
    "students" : [
        {
            "name" : "Dilan",
            "age" : 18
        },
        {
            "name" : "Anhar",
            "age" : 17
        }
    ]
}

print(type(data))

with open("api/data.json", "w") as file:
    json.dump(data, file, indent=3)

print(json.dumps(data, indent=2))


# Json - python
text = '''
{
    "country" : "Indonesia"
    "city : "Jakarta"
}
'''

print(text)
print(type(text))

#py_data = json.loads(text)
#print(py_data)
#print(type(py_data))
#print(py_data['country'])

with open("api/data.json", "r") as file:
    data1 = json.load(file)

print(data1)
print(type(data1))
print(data1['employees'])
print(data1['students'])