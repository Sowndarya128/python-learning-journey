numbers = [1,2,2,3,3,4]
duplicates = []
for n in numbers:
    if numbers.count(n) > 1 and n not in duplicates:
        duplicates.append(n)
print(duplicates) 