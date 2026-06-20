list1 = [1,2,3,4]
list2 = [2,3,4,5]
common =[]
for n in list1:
    if n in list2:
        common.append(n)
print(common)