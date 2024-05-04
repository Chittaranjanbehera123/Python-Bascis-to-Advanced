# String formatting in python:
# string Formatting can be done in python using the format Method.
txt = "For only {price:2f} dollars!"
print(txt.format(price=49))
#  f-string in python
val = "Geeks"
print(f"{val} for {val} is a portal for {val}.")
name='Chittaranjan'
age=23
print(f"Hello, my name is {name} and I'M  {age} years old.")

# Programm:
Letter = "Hey My name is {1} and I am from {0}"
country = "India"
name = "Chittaranjan"

print(Letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")
print(f"we use f-string like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.0999
txt = f"for only {price:2f} dollars!"
print(txt)

# Docstring in python
# Python docstring are the string Literals that appear right after the defination of a function, Method class or Module 
# Example1:
def anynubersquare(n):
    # ...Takes in a number n, returns the square of n....
    print(n**2)
anynubersquare(5)

# Example2:
def anynubersquare(n):
    # Takes in a number n, returns the square of n
    multiplication = n**2
    return multiplication

# Example usage:
user_input = int(input("Enter Your Number: "))
multiplication = anynubersquare(user_input)
print(f"The square of {user_input} is: {multiplication}")

# Python doc attribute 
# When ever string literals are present just after the defination of afunction, Module class or method they are associated with the object as their doc attribute, We can later use this attributes to  retrive this docstring 
# Example2:
# def square(n):
#     # ... Takes in a number n, returns the square of n... 
#     return n**2
# print(square:__doc__)