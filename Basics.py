# Basics Python
print("Hello ChittaranjanBehera")
print(5)
print("Bye")


# Comments, Escape Sequence &Print
"""
Hey Chintu, Please don't remove this line
Author: Chintu
Course: Python
"""
print("Hey I am\ 'a\"good boy\"\n and this viewer is also agood boy/girl")
print("Hello world")
# This is a 'Single-line comment'
print("This is a print statement.")


# Variables and Data Types
# Data types-Integer,Float,Boolean,str
a = complex(8,2)
b = True
c = "Chittaranjan"
print(a)
print(b)
a1 = 9
print(a+a1)
print("The type of a is", type(a))
print("The type of a is", type(b))
print("The type of a is", type(c))

# operators:
# Arithmetic Operators= +,-,*,/,etc
# Assignment Operators- =,+=,-=,etc
# Comparission Operators- ==,>=,<=,<,>,!=,
# Logical Operator- and,or,not
print(15+6)
print(15-6)
print(15*6)
print(15/6)
print(15//6)
print(5%3)
print(2**4)

a = 10
b = 25
sum = a+b
print(sum)

# Program: Calculating
a = 50 
b = 3
print("The value of",a,"+",3,"is:", a+b)
print("The value of",a,"-",3,"is:", a-b)
print("The value of",a,"*",3,"is:", a*b)
print("The value of",a,"/",3,"is:", a/b)

# Print() Function | Message 
# Printing & Variable Value
# printing
# The Print() Functions prints the given object to the standard output device (screen) or to the text stream file 
message="This is statement1"
print(message)
# objects: objects to the printed.* indicates that there may be more than one object.
# sep: it can be string that you want to place between values; otherwise, it will default to a space
# Print the string message
print('Python','is','Snake name')
print("sunday","Monday","Tuesday","Wednessday","Thrusday",sep="_")

call1 = "Python is snake name"
call2 = "Python is easy to learn"
print(call1, end=" ")
print(call2)

# Two Types of casting
# 1.Explict typecasting
# 2.Implict typecasting
# Examples of explict typecasting
string = "15"
Number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum = Number + string_number
print("The sum of these two numbers is:",sum)

# Examples of imlict type casting.
# Python automatically converts
# a to int
a = 7
print(type(a))
# Python automatically converts b to float
b = 3.0
print(type(b))
# Python automatically converts c to float as it is a float
sum = a+b
print(sum)
print(type(sum))

# Example
x = 1.2e3
print('value:',x)
print('data type:', type(x))
a = True
print(a,type(a))

# Example1:
# Str type
first_name = "Rohit"
last_name ="Sharma"
print(first_name,type(first_name))
print(last_name,type(last_name))

print('welcome')
print()
print(print())
print(())
#print(,)  #syntax error
print([])
print(print())
print("hello",print(),print())
print(print(),"hello",print())
print("hello","welcome")
print("hello","welcome",3435345)
#print(423423+"python") #type error
#Print("welcome")  #name error
print("welcome"+"python")

#comments (Documentation section)
# single line comments
''' multi-line
comment '''
""" multi-line
comment"""

print('"hello"')
print('''"hello"''')
print("'''hello'''")
print("It's raining today?")
print("'It's raining today?'")
print("'It\'s raining today?'")
import sys
print(sys.path)

# Types to check Datatype
# It is used to  check datatype of the variable
x = 10
print("value of x:",x)
print("Datatype of x:",type(x))

y = 12.36
print("value of y:", y)
print("Data type of y:",type(y))

z = "ITVedant"
print("value of z:",z)
print("Dtatype of z:",type(z))

# Big numbers
price = 232342_234563_567892_124563_456789_123567
print(price)

# Example4:
a="1"
b="2"
print(int(a)+int(b))

# implicit Typecasting
c=1.9
d=8
print(c+d)


# Example5:
a = input("Enter your Name:")
print("My name is",a)

x = input("Enter First number.")
y = input("Enter your Second Number.")
print(x+y)

print(int(x)+int(y))

# Example6:
# Pass arguments to the python Input function 
user_name = input("Enter your name:-")
print("Hi", user_name, "\b")

# int(): Int function is use to convert other datatype into integer
# Example7:
num1 = int(input("Enter First Number."))
num2 = int(input("Enter Second Number."))
result=num1+num2
print("Result",result)