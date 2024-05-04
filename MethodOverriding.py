# Method Overriding in Python: 
# Method Overriding is apowerful feature in object-oriented Programming that allows you to redefine a method in a derived class. The method in the derived class is said to Override the method in the base class when you create an instance of the derived class and call the overrideen Method the version of the method in the derived class is executed rather than the version in the base class   
# Example1:
class Shape:
    def area(self):
        pass  # You can provide a default implementation or make it abstract

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

# Example usage
circle = Circle(5)
print("Circle Area:", circle.area())

# Programm1:
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()

c = Circle(5)
print(c.area())

# Operator Overloading in Python: 
# Example1:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: " + type(other).__name__)

# Example usage
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)

# Programm1:
class vectors:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    
    def __add__(self, x):
        return vectors(self.i + x.i, self.j + x.j, self.k + x.k)

# Corrected instances
v1 = vectors(3, 5, 6)
print(v1)

v2 = vectors(1, 2, 9)
print(v2)

result = v1 + v2
print(result)
print(type(result))

# Single Inheritance In Python: 
# singlr inheritance is atype of inheritance where aclass inherits Properties and Behaviour from asingle Parent class. This is the simpled and most common from of inheritance 
# Examples1:
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

# Example usage
animal = Animal("Generic Animal", "Unknown Species")
animal.make_sound()

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)        # Accessing the attribute from the parent class
print(dog.species)      # Accessing the attribute from the parent class
print(dog.breed)        # Accessing the attribute specific to the Dog class
dog.make_sound()  

# Multiple Inheritance in python: 
# Multiple inheritance is a powerful features in object-oriented Programming that allows aclass inherit attributes and Methods from multiple Parent classes. This can be useful in situations where aclass needs to inherit functionality from Multiple sources 
# Example1: 
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.data}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

obj1 = DancerEmployee("Kathak","Shivani")
print(obj1.name)
print(obj1.dance)
obj1.show()
print(DancerEmployee.mro())

# Hierarchical Inheritance: 
# Hierarchical Inheritance is a type of inheritance in object Oriented Programming where Multiple Subclasses inherit from a single base class. In other words asingle base class acts as a parent class for multiple subclass This is way of establishing realtionship between classes in ahierarchical manner. 
# Example2:
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def Show_details(self):
#         print("Name", self.name)

# Example3:
# Example of Hybrid Inheritance 
# class BaseClass:
#     pass

# class Derived1(BaseClass):
#     pass

# class Derived2(BaseClass):
#     pass

# class Derived3(BaseClass):
#     pass

# # Hierarchical Inheritance
# class BaseClass:
#     pass