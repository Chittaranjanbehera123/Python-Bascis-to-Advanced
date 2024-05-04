def hello():
    print("hello")

hello()

rajeev = {
    'sales': 6000,
    'profit': 2000,
    'ad': 1000
}

vikrant = {
    'sales': 6000,
    'profit': 2000,
    'ad': 1000
}

# You can add more individuals with their respective data following the same pattern.

# Accessing the sales for Rajeev
rajeev_sales = rajeev['sales']
print("Rajeev's sales:", rajeev_sales)

# Accessing the sales for Vikrant
vikrant_sales = vikrant['sales']
print("Vikrant's sales:", vikrant_sales)

# Python class and objects: 
# A class is a blueprint or a template for creating objects providing intial values for state (member variables or attributes), and implementation of behavoiur (Member functions or methods) The user-defined objects are created using the class keywords 
# Creating aclass:
# class Details:
#     name = "Chintu"
#     age = 20

# Creating an objects: 
# object is instance of the class used to access the properties of the class Now lets Create an object of the class 
# Example1: 
class Details:
    name = "Chintu"
    age = 24
obj1 = Details()
print(obj1.name)
print(obj1.age)

# Self Parameter: 
# The self Parameter is areference to the current instance of the class, and is used to access variables that belongs to the class. 
# Examples1:
class Details:
    name = "Chittaranjan"
    age = 25
    
    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old")

obj1 = Details()
obj1.desc()

# Programm: 
class person:
    name = "Chintu"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
c = person()
a.name = "Chittaranjan"
a.occupation = "Accountant"

b.name = "Laharika"
b.occupation = "HR"
# print(a.name, a.occupation)
a.info()
b.info()

# Constructor: 
# A constructor is a special Method in a class used to create and intialize an object of a class. There are different types of constructor. constructor is invoked automatically when an object of a class is created. 
# Types of constructor in python 
# 1. Parameterized constructor 
# 2. Default constructor 
# 1.Ans: 
# when the constructor accepts arguments along with self it is known as parameterized constructor 
# These arguments can be used inside the class to assign the values to the data members 
# Example:
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("crab", "Circustanceans")
print(obj1.animal, "belong to the", obj1.group, "group")

# Default Constructor in python 
# When the constructor doesn't accept any arguments from the object and has only one argument, self self in the constructor , It has known as aDefault constructor 
# Example1:
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

class Default:
    def __init__(self):
        print("animal Crab belongs to Crustaceans group")

# Creating an instance of the Details class
obj1 = Details("crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group")

# Creating an instance of the Default class
obj2 = Default()

# Programm:
class person:
    def __init__(self, name, oce):
        print("Hey, I am a person")
        self.name = name
        self.oce = oce

    def info(self):
        print(f"{self.name} is a {self.oce}")

# Provide 'name' and 'oce' when creating an instance of the person class
a = person(name="Laharika", oce="HR")
print(a.name)
a.name = "Divya"
a.oce = "HR"
a.info()  # This will print "Divya is a HR"

# Python Decorators: 
# Python decorators are a powerful and versatitle tool that allow you to modify the behaviour of functions and Method They are a way to extend the functionality of a function or Method without modifying its source code  

# A decorator is a function that takes another function as an argument and returns anew function that that Modifies the behaviour of the orginal function. The new function is often referred to as a "decord" function. The basic syntax for using adecorder is the the following: 

# The @decorator_function notaion is Just ashorthand for the following code: 
# @decorator_function
def decorator_function(original_function):
    def wrapper():
        print(f"Executing {original_function.__name__}")
        original_function()
    return wrapper

@decorator_function
def my_function():
    print("Inside my_function")

my_function()

# Example1:
import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"calling {func.__name__} with args = {args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result

    return decorated

@log_function_call
def my_function(a, b):
    return a + b

# Example2:
def great(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this Function")
    return mfx

@great
def hello():
    print("Hello World")

def add(a, b):
    print(a + b)

hello()
great(add)(1, 2)


        
