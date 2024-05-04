# calculator(all aithmatic)
# calculating square and cube of integer number
# calculating area and perimeter of circle and rectangle
# calculte simple interest when principle_amount=5000, period=1yr and rate of interest=0.7%

# swpping numbers
a = int(input("enter a="))
b = int(input("enter b="))
print(f"Before swapping a={a} and b={b}")
# 1st way without using third variable
# a, b = b, a
# 2nd way without using third variable
# a = a + b  # a=9
# b = a - b  # 9-5=4
# a = a - b  # 9-4=5
# 3rd way with using third variable
c = a
a = b
b = c
print(f"After swapping a={a} and b={b}")

# # # WAP to take selling price and total price from user and show earned
# profit or loss earned by user
totalprice = float(input("enter total price="))
sp = float(input("enter selling price="))
print(f"You earned {sp-totalprice} Profit") if sp > totalprice else print(
    f"You got {totalprice-sp} Loss"
)


# Example:4
# calculating square and cube of integer number
# Ans:
# Get user input as an integer
number = int(input("Enter an integer: "))
# Calculate square and cube
square = number ** 2
cube = number ** 3
# Display the results
print(f"The square of {number} is: {square}")
print(f"The cube of {number} is: {cube}")


# Example5:
# calculating area and perimeter of circle and rectangle
import math

# For Circle
radius = float(input("Enter the radius of the circle: "))
circle_area = math.pi * radius ** 2
circle_perimeter = 2 * math.pi * radius

print(f"The area of the circle is: {circle_area}")
print(f"The perimeter (circumference) of the circle is: {circle_perimeter}")

# For Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

print(f"The area of the rectangle is: {rectangle_area}")
print(f"The perimeter of the rectangle is: {rectangle_perimeter}")