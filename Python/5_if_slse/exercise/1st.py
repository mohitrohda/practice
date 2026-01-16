'''
Write a program that asks user to enter a city name and it should tell which country the city belongs to
'''

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter the city name =").lower()

if city in india:
    print("City is in India")
elif city in pakistan:
    print("City in pakistan")
elif city in bangladesh:
    print("City in Bangladesh")
else:
    print("Given City is not in Country List")


'''
Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
For example if I enter mumbai and chennai,
it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
'''

city1 = input("Enter the 1st city name =").lower()
city2 = input("Enter the 2nd city name =").lower()

if city1 in india and city2 in india:
    print(f"{city1} and {city2} both are in india")
elif city1 in pakistan and city2 in pakistan: 
    print(f"{city1} and {city2} both are in pakistan")
elif city1 in bangladesh and city2 in bangladesh: 
    print(f"{city1} and {city2} both are in bangladesh")
else:
    print("They don't belong to same country")
           
