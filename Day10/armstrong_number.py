num = 371
temp = num
total = 0
while num> 0:
    digit = num % 10
    total += digit**3
    num = num // 10
print(total)