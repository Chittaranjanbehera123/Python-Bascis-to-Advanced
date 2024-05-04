# Access Specifiers/Modifiers
# Access Specifiers or acess modifiers in python Programming are used to limit the access of class variables and class
# Methods outside of class while implementing the concepts of inheritance. 
# Types of access Specifiers
# 1.Public access Specifiers
# 2.Private access Specifiers
# 3.Protected Access modifiers

# Public Access Specifiers in python:
# All the variable and Methods (member function) in python are by default public Any instance variable in a class followed by 'self' 
# keyword i.e self.var_name are public accessed 
# Example1:
class student:
    # constructor is defined 
   def __init__(self, age, name):
       self.name=name # Public Variable
       self.age=age   # Public Variable
       
obj = student(24,"Chittaranjan")
print(obj.name)
print(obj.age)

# Private Access Modifiers:
# Example2:
class Student:
    def __init__(self, age, name):
        self.__age = age  # Double underscore indicates a private variable
        self.__name = name  # Adding a private variable for name

    def __funName(self):  # Double underscore indicates a private method
        print(f"Hello, my name is {self.__name}.")

# Creating an object of the Student class
obj = Student(age=20, name="John")

# Accessing private variables
print(obj._Student__age)  # Accessing private variable __age (not recommended)

# Calling a private method
obj._Student__funName()  # Calling private method __funName (not recommended)

# Protected Example3:
class Students:
    def __init__(self):
        self._name = "Chittaranjan"

    def _funName(self):  # Protected Method
        return "CodewithChitta"

class Subject(Students):
    pass

# creating an instance of the Subject class
obj1 = Subject()

# calling by object of Students class
obj = Students()
print(obj._name)
print(obj._funName())

# calling by object of Subject class
print(obj1._name)
print(obj1._funName())