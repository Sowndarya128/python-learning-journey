with open("sample.txt", "r") as file:
    count = len(file.readlines())
print(count)