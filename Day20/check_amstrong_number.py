num = 153
total = 0 
temp = num
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp = temp // 10
if total == num:
    print("Amstrong")
else:
    print("Not amstrong")