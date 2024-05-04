# Super Keyword in Python: 
# The super() keyword in python is used to refer to the parent class. It is especially useful when aclass inherits from multiple parent class and you want to call amethod from one of the parent class    
# Example1:
class ParentClass:
    def Parent_method(delf):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method")

        super().Parent_method()

child_object = ChildClass()
child_object.child_method()

# Programm1:
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name,id)
        self.lang = lang

rohan = Employee("Rohan Das","420")
harry = Programmer("Chintu", "2345", "Python")

print(harry.name)
print(harry.id)
print(harry.lang)

# Magic/Daunder Methods in Python: 
# Example1: 
class Employee:
    name = "Harry"
    def __Len__(self):
        i = 0
        for i in self.name:
            i = i+1
            return i
        
def __str__(self):
    return f"The name of the employee is {self.name} str"
def __repr__(self):
    return f"Employee('{self.name}')"

def __call__(self):
    print("Hey I am good")