sentence = "python python is easy"
word = sentence.split()
freq = {}
for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)