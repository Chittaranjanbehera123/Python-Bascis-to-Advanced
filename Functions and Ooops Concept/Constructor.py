# Constructor:
# A constructor is a special Method in a class used to  create and intialize an object of a class . 
# Example:
class Person:
    def __init__(self, name, occ):
        print("Hey I am a Person") 
        self.name = name
        self.occ = occ
        
    def info(self):
      print(f"{self.name} is a {self.occ}")
    
    
a = Person("Chittaranjan", "Developer")
b = Person("Divya","HR")
a.info()
b.info()

# Types of Constructor 
# 1. Parameterized Constructor
# 2. Default Constructor

# Parameterized Constructor
# When the constructor accepts arguments along with self it is known as parameterized constructor .
# Example1:
class Car:
    def __init__(self, animal, group):
        self.animal=animal
        self.group=group
        
    def info(self):
      print(f"{self.animal} is a {self.group}")
      
object1=Car("Crab","Crustances")
object1.info()
    
    
# Default Constructor in Python:
# When the constructor doesn't accept the any arguments from the object and has only one arguments Self in the constructor. 
class Default:
    def __init__(self):
        print("animal Crab belongs to Crustances group") 
        
obj1 = Default()   