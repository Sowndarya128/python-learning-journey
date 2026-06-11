import re
text = "My number is 987654321"
result = re.findall(r"\d",text)
print(result)