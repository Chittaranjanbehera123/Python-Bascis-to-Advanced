# How importing in python works: 
import math
result = math.sqrt(9)
print(result)

# from keyword: 
# you can also import Specific functions or variables from a module using the from keyword. for example to import only the sqrt function from the math module you would write. 
from math import sqrt, pi
result = sqrt(9)
print(result)
print(pi)

# import everything: 
from math import*
result = sqrt(9)
print(result)
print(pi)

# The "as" Keyword 
import math as m
result = m.sqrt(9)
print(result)
print(m.pi)

# The dir function():
# Programm1:
# from math import sqrt, pi
# from math import sqrt as s, pi
# import math as math_builtin_python
# # import chintu as hr

# print(dir(math_builtin_python))  # Use the correct module name here
# print(math_builtin_python.nan, type(math_builtin_python.nan))  # Use the correct module name here
# hr.welcome()
# print(hr.chintu)

# if name==main in python 
# if "__name__==__main__" in python 

# The if__name__=="__main__" idom is a common pattern used in python Scripts to determine whether the script is being run directly or being import as a mpdule into another Script 

