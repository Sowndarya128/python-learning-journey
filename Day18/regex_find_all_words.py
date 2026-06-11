import re
text = "My number is 987654321"
result = re.findall(r"\w+",text)
print(result)