import json
data = '{ "name": "Sowndaraya","age": "22"}'
student = json.loads(data)
print(student["name"])