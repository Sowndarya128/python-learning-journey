text = "Python is easy"
word = text.split()
largest = max(word, key=len)
print(largest)