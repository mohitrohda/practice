'''
Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal
'''

sugar_lvl = input("Enter your fasting Sugar level =")
sugar_lvl = float(sugar_lvl)

if sugar_lvl < 80:
    print("your sugar level is low")
elif sugar_lvl > 100:   
    print("your sugar level is high")
else:
    print("your sugar level is mormal")     
