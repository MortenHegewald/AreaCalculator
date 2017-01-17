import math

# Ask user which shape they want calculated
shape = input("Are you looking at a triangle, square or a circle?")

if shape == "triangle":
    height = input("What is the height of your triangle?")
    width = input("What is the width of your triangle?")
    area = int(height) * int(width) / 2
    print("The area of your triangle is " + str(area) + ".")
if shape == "square":
    height = input("What is the height of your square?")
    width = input("What is the width of your square?")
    area = int(height) * int(width)
    print("The area of your square is " + str(area) + ".")
if shape == "circle":
    rad = input("What is the radius of your circel?")
    area = math.pi * int(rad) * int(rad)
    print("The area of your circle is " + str(area) + ".")
elif shape != "triangle" and shape != "square" and shape != "circle":
    print("Sorry, I do not know that shape.")