x = input("Enter number 1 =")
y = input("Enter number 2 =")

try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print("division by zero error")
    z = None
except TypeError as e:
    print("Type Error ocuured")
    z = None

print("Division is:", z)    