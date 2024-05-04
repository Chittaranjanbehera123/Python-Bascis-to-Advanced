# Inheritance:
# when a class derived from another class the child class will inherit all the public and procted properties and methods from the parent class  
# Example1:
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def showDetails(self):
        print(f"The name of the Employee: {self.id} is {self.name}")
        

class Programmer(Employee):
    def showLanguage(self):
        print("The Default language is Python")

e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Chittaranjan", 4100)
e2.showDetails()
e2.showLanguage()

# Single Inheritance in Python:
# single inheritance is a type of inheritance where aclass inherits Properties and behaviours from asingle parent class. This is the simplest and most common from of inheritance 
# Example1:
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("sound made by the animal")
    
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
    
 
d = Dog("Dog", "Doggerman")
d.make_sound()   

a = Animal("Dog", "Dog")
a.make_sound()

# Multiple Inheritance in Python: 
# multiple inheritance is a powerful feature in object-oriented Programming that allows aclass to inherit attributes and methods from multiple Parent classes. This can be useful in situations where aclass needs to inherit functionality from multiple sources 
# Example1:
class Employee:
    def __init__(self, name):
        self.name= name
        
    def show(self):
        print(f"The name is {self.name}")
        
class Dancer:
    def __init__(self, dance):
        self.dance = dance
        
def show(self):
    print(f"The dance is {self.data}")
    
class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance=dance
        self.name=name
        
o=DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())

# Hierarchical Inheritance:
# Hierarchical Inheritance is a type of inheritance in object-oriented Programming where multiple Subclasses inherit from a single base class. In other words, asingle base class acts as a Parent class for multiple subclass. 
# Example3:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Abstract method, to be overridden by subclasses

class Mammal(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def speak(self):
        return f"{self.name} the mammal says {self.sound}"

class Bird(Animal):
    def __init__(self, name, song):
        super().__init__(name)
        self.song = song

    def speak(self):
        return f"{self.name} the bird sings {self.song}"

# Creating instances of the classes
lion = Mammal("Leo", "roar")
sparrow = Bird("Sparrow", "chirp")

# Using the speak method
print(lion.speak())    # Output: Leo the mammal says roar
print(sparrow.speak())  # Output: Sparrow the bird sings chirp
