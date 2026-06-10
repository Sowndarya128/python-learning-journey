numbers = [1,2,3,2,1,2,4,5,4]
freq = {}
for n in numbers:
    if n in freq:
        freq[n] +=1 
    else: 
        freq[n] = 1
print(freq)