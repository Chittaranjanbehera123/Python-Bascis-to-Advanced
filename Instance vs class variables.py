# isinstance vs class variables: 
# In python, Variables can be defined at the class level or at the instance level. understanding the difference between these types of variables is crucial for writing efficient and maintainble code 
# Class variables: 
# class variable are defined at the class level and are shared among all instances of the class . They are defined outside of any method and are usally used to store inform action that is common to all instances of the class. for examples aclass variable can be used to store the number of instances that have been created. 
class Myclass: #[Dout]
    class_variable = 0

    def __init__(self):
        Myclass.class_variable += 1

    def print_class_variable(self):
        print(Myclass.class_variable)

# Instantiate objects outside the class
obj1 = Myclass()
obj2 = Myclass()

# Call methods on the objects
obj1.print_class_variable()
obj2.print_class_variable()

# Instance Variable: 
# Instance variables are defined at the instance level and are unique to each instance of the class . They are defined inside the init method and are usually used to store information that is Specific to each instance of the class For example, an instance variable can be used to Store the name of an employee in a class that represents an example 
# Example1:
class MyClass:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

# Instantiate objects outside the class
obj1 = MyClass("Chittaranjan")
obj2 = MyClass("Behera")

# Call methods on the objects
obj1.print_name()
obj2.print_name()

# Programm1: 
class Employee:
    CompanyName = "Apple"
    noOfEmployee = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployee += 1

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.CompanyName} is {self.raise_amount}")

# Create an instance of the Employee class
emp1 = Employee("Chintu")

# Modify instance attributes
emp1.raise_amount = 0.3
emp1.CompanyName = "Apple India"

# Call the showDetails method
emp1.showDetails()

# Exercise1:
# write aLibrary class with no_of_books and books as two instance variables.Write aProgramm to create a Library from this Library class and show how you can print all books and book and get the number of books using different Methods. show that your Programm doesn't Persists the books after the programm is stopped. 
# Programm1:
class Library:
    def __init__(self):
        self.noBooks = 0 
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.noBooks} books. The books are {', '.join(self.books)}")

# Create an instance of the Library class
L1 = Library()

# Add books to the library
L1.addBook("Harry Potters1")
L1.addBook("Harry Potters")

# Display library information
L1.showInfo()

# How to use Python class Methods: 
# Example1: 
class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and Company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

# Create an instance of the Employee class
e1 = Employee()
e1.name = "Chintu"
e1.show()
# Call the changeCompany class method
Employee.changeCompany("Tesla")
# Display updated information
e1.show()
print(Employee.company)

# The dir() method: 
# dir(): The dir() function returns a list of all the attribute and methods including dunder methods avialable for an object . It is a Useful tool for Dicovering what you can do an object. 
# Example1: 
x = (1,2,3)
print(dir(x))
print(x.__add__)

# The__dict__attribute:
# __dict__: The__dict__attribute returns a dictionary representation of an objects attribute. It is a useful tool for intrduction 
# Example1: 
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.version = 1

P = Person("Chittaranjan", 24)
print(P.__dict__)

# The help() Method:
# help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods 
# Example2:
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


P = person("Chittaranjan",30)
print(P.__dict__)

print(help(person))

