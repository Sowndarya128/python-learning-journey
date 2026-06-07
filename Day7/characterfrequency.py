name = "Sowndarya"
count = {}
for ch in name:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1
print(count)

