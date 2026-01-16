'''
Write a function called calculate_area that takes base and height as an input and returns and area of a triangle
Equation of an area of a triangle is,
area = (1/2)*base*height
'''

def calculate_area(base,height,shape = "triangle"):

    if shape == "triangle":
        area = (1/2) * base * height
        return area
    elif shape == "rectangle":
        area = base * height
        return area
    else :
       # raise ValueError("Invalid shape type. Choose 'triangle' or 'rectangle'.")
       print("none")

          
    
    

base = 5
height = 10

print("The area of triangle =",calculate_area(base,height,"triangle"))
print("The area of triangle =",calculate_area(base,height,"rectangle"))