'''
Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print

*
**
***
****
'''

def print_pattern(a=0):
    s = int(input("enter input = "))
    for i in range(1,s+1):
        s = " "
        for j in range(i):
            s += "*"
        print(s)


pattern = print_pattern()
print(pattern)

