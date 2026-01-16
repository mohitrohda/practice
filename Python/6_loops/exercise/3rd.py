'''
Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
If expense is not found then it should print that as well.
'''

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["Jan","Feb","Mar","April","May"]

amt = input("Enter the Amount =")
amt = int(amt)

month = 1
for i in range(len(expense_list)):
    if amt == expense_list[i]:
        month = i
        break

if month == i:
    print(f"you spent {amt} in {month_list[month]}")
else:
    print(f"You didn't spend {amt} in any month")    