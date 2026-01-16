'''Write a program that prints following shape

*
**
***
****
***** '''
n = int(input("Enter a no of rows ="))

for i in range(1,n+1):
    s = ""
    for j in range(i):
        s += "*"
    print(s)

    