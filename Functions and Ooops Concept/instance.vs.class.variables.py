# class variables:
# The class variables defined as the class level and among all the instance of the class. They are defined as the outside of the method and usually store the information that is common to all instance of the class.

# Instance vs class variables:
# In python, variable can be defined at the class level or at the instance level. understanding the difference between these types of variables is crucial for writting efficient and maintainble code 
# Example2:
class Employee:
    companyName = "Apple"
    noofEmployee = 0
    def __init__(self, name):
        self.name = name
        self.raise__amount = 0.02
        Employee.noofEmployee +=1
        
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in{self.noofEmployee}sized {self.companyName} is {self.raise__amount}")
        
        
# Employee.showDetails(emp1)
emp1 = Employee("Chittaranjan")
emp1.raise__amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

# Example3:
class Myclass:
    class_variable = 0
    
    def __init__(self):
        Myclass.class_variable += 1
    
    def print_class_variable(self):
        print(Myclass.class_variable)
    
obj1 = Myclass()
obj2 = Myclass()

obj1.print_class_variable() 
obj2.print_class_variable()