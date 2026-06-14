try:
    num = int("abc")
    print(num)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")