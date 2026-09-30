import json
# JSON & Structured Data
# They're very similar, but JSON is a data format, while the Python version is a Python object.
# Just like Go has marshal and unmarshal. The Python MODULE JSON also has it's functions responsible for converting to Json and vice-versa.
# json.dump() >> python > json file
# json.dumps() >> python > json string
# json.load() >> json file > python
# json.loads() >> json string > python


# python dictionary to json string
developer = {
    "name": "Jerrie",
    "age": 25,
    "language": "Python"
}

json_data = json.dumps(developer, indent=2)

print(json_data)

# Json string to python object 
json_data = '{"name": "Jerrie", "age": 25}'

developer = json.loads(json_data)
print(developer)

developers = {
    "name": "Jerrie",
    "age": 25,
    "language": "Python"
}

with open("developer.json", "w") as file:
    json.dump(developers, file, indent=2)