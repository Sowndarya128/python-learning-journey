numbers = [6,90,5,99,8,100]
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print(smallest)