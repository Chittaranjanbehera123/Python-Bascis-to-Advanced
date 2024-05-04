# python function:
# A function is a block of code that perfroms a specific task whenever it is called . In Bigger Programms where we have large amount of codes
# There are two types of Functions
# 1. Built in functions
# 2. user-defined Functions


# 1.Ans:
# These functions are defined in precoded in python. some examples of built-in functions 
# main(),len(),max(),min(),list(),tup(),set(),sum(),dict(),print()


# 2.Ans:
# We can create functions to perform specific task as per our needs. such functions are called user-defined functions

# calling functions
# Ans: We can call a function by giving a function name, followed by parameters (if any) in the parathensis 
# Example1:
def name(firstname, lastname):
    print("Hello",firstname,lastname)
    
name("chittaranjan","Behera")

# Example2:
import math

def calculateGmean(a, b):
    Mean = math.sqrt(a * b)
    print(Mean)
    
calculateGmean(4, 9)
    
def isGreater(a, b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater")

# Example usage
isGreater(10, 5)

# Example2:
def average(a,b):
    print("The average is", (a+b)/2)
    
average(4,6)

# Functions Arguments and return statement:
# There are four types of arguments
# 1.Default Argument
# 2.Keyword Argument
# 3.variable length Argument
# 4.Required Arguments

# 1.Ans:
# Example1:
# Default arguments:
# We can provide a default arguments  while creating a function this a way the function assumes adefault value  even if a value is not provided in the function call or that arguments
def average(a=9,b=1):
    print("The average is", (a+b)/2)
    
average(b=9)

# Example2:
def name(fname,mname="ranjan",lname="Behera"):
    print("Hello",fname,mname,lname)
    
name("Chitta")

# keyword arguments:
# We can provide arguments with key value , this way the interpreter recognizes the arguments by the parameter name. Hence the Order in which the arguments are passed does not matter
# Example2:
def name(fname,mname,lname):
    print("hello",fname,mname,lname)

name(mname="Ranjan",fname="Chitta",lname="Behera")

# Required Arguments:
# In case we don't pass the arguments with key value=value syntax then it is necessary to pass the arguments in the correct possitional order and the number of arguments passed should match with actual function definition
# Example2:
def average(a, b, c=1):
    print("The average is",(a+b+c)/2)
    
average(5, 6)

# Variable length Arguments
# sometimes we may need to pass more arguments than those defined in the actual function .This can be done using variable length arguments.
# Example1:
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i

    print("Average is:", sum/len(numbers))

average(5, 6, 7, 1)

# There are two ways to acheive this:
# Arbitary Arguments
# While Creating afunction pass a before the parameter name while creating the function. The function access the argument by processing them in the form of tuple 
# Example1:
# Example1:
def name(*name):
    print("Hello",name[0],name[1],name[2])
    
name("Chitta","Ranjan","Behera")

# Keyword Arbitary Arguments:
# While creating afunction, pass a * before the parameter name while defining the function. The function access the arguments by processing them in the form of dictionary. 
# Example:
def name(**name):
    print("Hello",name["fname"],name["mname"],name["lname"])
    
name(mname="chitta",lname="Behera",fname="Chitta")

# Return Statement:
# The return Statement is used to return the value of the expression back to the calling functions 
# Example2:
def name(fname,mname,lname):
    return "Hello," + fname + " " +mname+ " " + lname

print(name("Chitta","Ranjan","Behera"))