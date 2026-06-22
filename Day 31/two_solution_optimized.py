#Brute Force solution(O(n^2))
numbers = [2, 7, 10, 13]
target = 9
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(i,j)

#Optimized solution(Hash map)
numbers = [2, 7, 10, 13]
target = 9
seen = {}
for i,num in enumerate(numbers):
    complement = target - num
     
    if complement in seen:
        print(seen[complement], i)
        break
    seen[num] = i