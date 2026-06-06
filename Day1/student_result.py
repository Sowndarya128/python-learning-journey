name = input("Enter your name")
m1 = int(input("enter your 1st marks:"))
m2 = int(input("enter your 2nd marks:"))
m3 = int(input("enter your 3rd marks:"))
average = ((m1+m2+m3)/3)
print("Name",name)
print("average",average)
if average>=90:
    print("Exellent")
elif 75<=average<=89:
    print("Very good")
elif 60<=average<=74:
    print("good")
elif 40<=average<=59:
    print("pass")
else:
    print("fail")