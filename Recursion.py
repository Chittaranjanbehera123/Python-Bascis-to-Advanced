# Recursion in Python
# Recursion is the Process of defining something in terms of itself 
#  A physical word example would be to place two parallel Mirrors facing each other. Any object in between them would be reflected recursive 
# Python Recursive Function 
# In Python, we know that function can call other function it is even possible for the function to call itself These types of construct are termed as recursive 
# Example1:
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Driver code
num = 7
print("Number:", num)
print("Factorial:", factorial(num))
