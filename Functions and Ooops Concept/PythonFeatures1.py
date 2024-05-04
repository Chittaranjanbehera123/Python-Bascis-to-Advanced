# Python class and objects
# A class is blueprint or template for creating objects Provided intial values. that is called python class 

# object:
# Object is a instance of class access the properties of the class create an object
# Example1
class Details:
    name="Chittaranjan"
    age=20

Details.name = "Chintu" # update
Details.age = 24       # update
print(Details.name) 
print(Details.age)

# Example2:
class Details1:
    name = "Chittaranjan"
    age = 24
    
object1=Details1()
object1.name="Rohan"
object1.age="20"

print(Details1.name)
print(Details1.age)

# Example2:
class Details:
    name = "Sunakar Behera"
    age = 32
    
object1=Details()
print(object1.name)
print(object1.age)

# Example3:
class person:
    name = "Chittaranjan"
    occupation = "software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
a = person()
b = person()
a.name = "shubham"
a.occupation = "Accountant"

b.name = "Nikita"
b.occupation = "HR"

a.info()
b.info()

# Self parameter:
# The self pararmeter is areference to the current instance of the class and is used to access variables that belongs to the class.
# Example1:
class Details1:
    name = "Chittaranjan"
    age = 20
    
    def desc(self):
        print("My name is", self.name, "and I am", self.age, "years old")

object1 = Details1()
object1.desc()