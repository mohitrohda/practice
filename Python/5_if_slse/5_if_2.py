italian = ["pasta","pizza"]
indian= ["biryani","dosa","paneer butter masala"]
american= ["burger","hot dog",]

dish= input("enter the dish name : ").lower()

if dish in italian:
    print("Dish is Italian")
elif dish in indian:
    print("Dish is Indian")
elif dish in american:
    print("Dish is American")
else:
    print("dish is not in system")    


