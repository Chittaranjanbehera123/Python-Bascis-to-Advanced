# Python try....except 
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer")

# Programm1:
n=input("Enter the number:")
print("Multiplication table of {n} is:")

try:
    for i in range(1,11):
        print(f"{int(n)} * {i} = {int(n) * i}")
except ValueError:
    print("Invalid input")

print("some imp. lines of code")
print("End of the code")
try:
    num = int(input("Enter an integer:"))
    a = [6, 3]
    print(a[num])

except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Index Error")

# Finally clause:
# The Finally code block is also apart exception handling when we handle exception using the try and except block, we can include afinally block at the end. The finally block is always executed. 
# Programm1: 
def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occuered")
        return 0
    finally:
        print("I am always executed")


x = func1()
print(x)

# Raising Custom errors: 
# In python, We can raise custom errors by using the 'raise' keyword 
Salary = int(input("Enter salary amount: "))
if not 2000<Salary<5000:
    raise ValueError("Not valid salary")

# If...Else in one Line: 
# There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short Here's an example 
a = 2 
b = 330
print("A") if a>b else print("B")

# Example:
# one line if else Statement, with 3 condition 
a = 330
b = 330
print("A") if a>b else print("=") if a==b else print("B")

# Enumerate function in python: 
# The enumerate function is a built-in function in python that allows you to loop over asequence (such as alist,tuple, or string) and get the index and value of each element in the sequence at the same time Here's basic example of how it works 
# loop over alist and print the index and value of each element 
# Example2:
fruits = ['apple','banana','Mango']
for index, fruit in enumerate(fruits):
    print(index,fruit)
print("The next line is:")

# change the start index:
fruits = ['apple','banana','Mango']
for index, fruit in enumerate(fruits,start=1):
    print(index,fruit)   