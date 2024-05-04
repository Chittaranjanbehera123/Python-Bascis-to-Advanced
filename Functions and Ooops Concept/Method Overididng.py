# Method Overiding:
# Method Overiding is a powerful features in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to be override the method in the base class . 
# Example3:
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

# Instantiate Circle outside the class definition
c = Circle(5)
print(c.area())