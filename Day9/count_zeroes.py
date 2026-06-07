num = 2004
count = 0
while num>0:
    digit = num % 10
    if digit == 0:
        count += 1
    num = num // 10
print(count)