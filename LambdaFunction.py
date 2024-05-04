# Lambda Function in Python: 
# In python, alambda function is small anonymous function without a name It is defined using the Lamda key word and has the following syntax. 
# lambda arguments: expression
# Example1:
def appl(fx, value):
    return 6+fx(value)

double = lambda x:x*2
cube = lambda x:x*x*x
avg = lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(5))
print(avg(3,5,10))
print(appl(lambda x:x*x*x,2))

# Map:
# The map function appilication afunction to each element  in sequence and returns anew sequence containing the transform elements , The map function has the following syntax: 
# map(function, iterable)
# Example1:
numbers = [1,2,3,4,5]
doubled = map(lambda x:x*2,numbers)
print(list(doubled))

# filter:
# The filter function filters a sequence of elements based on given predicate (a function that returns aboolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:
numbers = [1,2,3,4,5]
evens = filter(lambda x:x%2 == 0, numbers)

# reduce:
# The reduce function is ahigher-order function that applies afunction to a sequence and returns asingle value It is a part of the functools module in python and has the following syntax:
# reduce(function, iterable)
# Example1:
from functools import reduce
numbers = [1,2,3,4,5]
# calculate the sum of the numbers using the reduce function 
sum = reduce(lambda x,y:x+y, numbers)
print(sum)

# Example1:
#MAP
L = [1, 2, 4, 6, 4, 3]
newL = list(map(lambda x: x*x*x, L))
# FILTER
def filter_function(a):
    return a>2

newnewL=list(filter(filter_function,L))
print(newnewL)

from functools import reduce

#List of Numbers
numbers = [1,2,3,4,5]

# Calculate the sum of the numbers using the reduce functions
def mysum(x,y):
    return x+y

sum = reduce(mysum, numbers)
print(sum)