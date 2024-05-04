# import time

# # Get the current time in the format HH:MM:SS
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)

# # Get the current hour
# timestamp = time.strftime('%H')
# print(timestamp)

# # Get the current minute
# timestamp = time.strftime('%M')
# print(timestamp)

# # Get the current time in seconds since the epoch (January 1, 1970)
# timestamp = time.strftime('%s')
# print(timestamp)

import time

# Get the current time in the format HH:MM:SS
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

# # Get the current hour
timestamp = time.strftime('%H')
print(timestamp)

# # Get the current minute
timestamp = time.strftime('%M')
print(timestamp)

# # Get the current time in seconds since the epoch (January 1, 1970)
timestamp = int(time.time())
print(timestamp)

# # Example:
sal = int(input("Enter your salary:"))
if(sal<=10000):
    print("No tax")
elif(sal>10000 and sal<=20000):
    tax = (0.10*sal)
    print(f"Tax Amount: {tax}")
elif(sal>20000 and sal<=30000):
    tax = (0.20*sal)
    print(f"Tax Amount:{tax}")
else:
    tax =(0.20*sal)
    print(f"Tax Amount:{tax}")

# # Example2:
# while Puechasing certain items, a discount of 10% is offered if the quantity Purchased is More than 1000. if Quantity and price 
# per items are input through the keyboard, write a program to calculate the total expense?
    
# Calculation of total expense
quantity = int(input("Enter the quantity purchased: "))
price_per_item = float(input("Enter the price per item: "))

if (quantity > 1000):
    discount_percentage = 10
    discount = (discount_percentage / 100) * (quantity * price_per_item)
else:
    discount = 0

total_expense = quantity * price_per_item - discount

print(f"Quantity: {quantity}")
print(f"Price per item: ${price_per_item:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Total Expense: ${total_expense:.2f}")



# Example2: Print the roots of the quadratic equation with comments. Write python code
import math

# Input coefficients
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the nature of the roots
if discriminant > 0:
    # Two distinct real roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two distinct real roots: {root1} and {root2}")

elif discriminant == 0:
    # One real root (double root)
    root = -b / (2*a)
    print(f"One real root (double root): {root}")

else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print(f"Complex roots: {root1} and {root2}")

# # Example3:
# WAP in Python to findout greatest among three numbers:
a =int(input("Enter input a three numbers:"))
b =int(input("Enter input a three numbers:"))
c =int(input("Enter input a three numbers:"))

if((a>b) and (a>c)):
    print("The Number is greater: {a}")
elif((b>a) and (b>c)):
    print("The Number is greater: {b}")
else:
      print("The Number is greater: {c}")

# # Example4:
# Any integer is input through the keyboard write a Program to find out wheather it is odd number or even number
Num =int(input("Enter your Number:"))
if(Num%2==0):
    print("The Number is even")
else:
    print("The Number is odd")

# Example5:
a = 6000

if a >= 400:
    b = 300
    c = 200
    print(f"The values are: {b} and {c}")
else:
    print("Condition not met.")

# Example6:
x = 10
y = 20

if x == y:
    print(f"The values are: {x} and {y}")
else:
    print(f"The values are not equal. x is {x}, and y is {y}")

# Example7:
    x =3
    y =3.0
    if(x==y):
        print("x and y equal")
    else:
        print("x and y are not equal")

# # Example8:[Dout]
        x=3
        y=x=10
        z=x<10
        print("The value of:{x} and {y} and {z}")
        
# Example9:
i=65
j='A'
if(chr(i)==j):
    print("Python is wow")
else:
    print("Python is headache")

# Example10:
a=12.25
b=12.52
if(a==b):
    print("a and b are equal")

# Example11:
j=10
k=12
if(k>=j):
    k=j
    j=k
    
# Example12:
# If the ages of Ram, Shyam and Ajay are input through the keyboard write a program to determine the youngest of the three?
Ram =int(input("Enter age of Ram"))
Shyam =int(input("Enter age of Shyam"))
Ajay =int(input("Enter age of Ajay"))
if(Ram<Shyam):
    if(Ram<Ajay):
        yong = Ram
    else:
        yong = Ajay
else:
    if(Shyam<Ajay):
        yong = Shyam
    else:
        yong = Ajay
        print("The Yong of Ram:{Ram}")
        print("The Yong of Shyam:{Shyam}")
        print("The Yong of Ajay:{Ajay}")

# Example13:
i=5
j=6
if(i<j):
    print("Hello")
    print("Hii")
    print("Hello")

# Example14:
i=5
j=6
if(i<j):
    print("Hello")
elif(j<i):
    print("Hii")
else:
    print("Fakir Mohan University")

# Example15:
i=5
j=6
if(i<j):
    print("Hello")
else:
    print("Hii")
    print("Welcome")