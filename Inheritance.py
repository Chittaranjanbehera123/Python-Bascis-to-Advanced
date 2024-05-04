# Python Inheritance Syntax:
# class BaseClass:
#     # Body of base class 
#     class DeriveClass(BaseClass):
#         # body of Deriveclass
# Types of Inheritance: 
# 1. Single inheritance 
# 2.Multi inheritance 
# 3. Hierarchical Inheritance 
# 4. Hybrid Inheritance
# Programm: 
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")

class Programmer(Employee):
    def showLanguage(self):
        print("The Default Language is Python")

e1 = Employee("Rohan Das", 400)
e1.showDetails()

e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()

# Public Access Specific in Python 
# All the variables and methods (member function) in python are by default public any instance variable in aclass followed by the 'self' keyword self.var_name are public accessed 
# Example: 
class student:
    # constructor is defined 
    def __init__(self, age, name):
        self.age = age # Public variable
        self.name = name # Public variable

obj = student(24, "Chintu")
print(obj.age)
print(obj.name)

# Private Access Modifier: 
# By definition, Private members of a class (variable or methods) are those members which are only accessible inside the class We cannot use private Members outside of class 
# Example1:
class student:
    def __init__(self, age, name):
        self.__age = age # An indication of Private variable
    def __funName(self):
     print(obj.__funName())
# calling by object of class subject
     print(obj.__age)
     print(obj.__funName)

# Protected Access Modifiers: 
# In object-oriented Programming (oop) , the term protected is used to describe amember (i.e a method attribute of a class that is intended to be accessed only by the class itself and its subclass . In python convention for indicating that is members protected 
# Example1:
class students:
    def __init__(self):
        self.__name = "Chintu"

    def _funName(self):  # Protected Method
        return "Codewithharry"


class Subject(students):  # Corrected the inheritance
    pass

obj = students()
obj1 = Subject()

# calling by object of student class
# print(obj.__name)
print(obj._funName())  # Accessing the protected method using a single underscore
# calling by object of subject class
# print(obj1.__name)
print(obj1._funName())  # Accessing the protected method using a single underscor

# static Methods: 
# Example1:
class Math:
    @staticmethod
    def add(a, b):
        return a + b

# Outside the class definition
result = Math.add(1, 2)
print(result)

# Programm: 
class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):  # Correct indentation
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b

# result = Math.add(1, 2)  # Uncomment this if needed
# print(result)

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

# Instance vs class variables: 
# In python, variables can be defined at the class level or at the instance level. understanding the differenece between these types of variable is crucial for writing efficient and maintainble code 
