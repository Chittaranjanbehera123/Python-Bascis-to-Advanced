# Datatypes:-determines type of value
# Built-in Datatypes
# (Numbers) int,float,complex
# (String)-str
# (Boolean)-bool(True,False)
# None
# (Collections)-tuple,list,set,dict(dictionary)

# int
i = 2343
print("i=", i, "Typeof i", type(i))
print(f"i={i} typeof(i)={type(i)}")
j = 4234_54353_23345345345_4234
print(f"j={j} typeof(j)={type(j)}")
#  float
print("---------float-----------")
i = 2343.5454
print(f"i={i} typeof(i)={type(i)}")
j = 4234_5.4353_23345345345_4234
print(f"j={j} typeof(j)={type(j)}")
# string
print("---------string-----------")
i = "welcome13232#$"
print(f"i={i} typeof(i)={type(i)}")
j = "python, java"
print(f"j={j} typeof(j)={type(j)}")
k = ""
print(f"k={k} typeof(k)={type(k)}")
# complex (use j for imaginary number)
print("---------complex-----------")
n1 = 5j
print(f"n1={n1} typeof(n1)={type(n1)}")
n2 = 0j
print(f"n2={n2} typeof(n2)={type(n2)}")
n3 = 8 + 6j
print(f"n3={n3} typeof(n3)={type(n3)}")
# boolean
print("---------bool-----------")
n1 = True
print(f"n1={n1} typeof(n1)={type(n1)}")
n1 = False
print(f"n1={n1} typeof(n1)={type(n1)}")
n1 = "True"
print(f"n1={n1} typeof(n1)={type(n1)}")

# None
print("---------NoneType-----------")
n1 = None
print(f"n1={n1} typeof(n1)={type(n1)}")
n1 = "None"
print(f"n1={n1} typeof(n1)={type(n1)}")

# Collection Data Types
print("---------tuple-----------")
n1 = (1, 2.1, True, "hello", 5j)
print(f"n1={n1} typeof(n1)={type(n1)}")
n1 = "hi", 56, "welcome"
print(f"n1={n1} typeof(n1)={type(n1)}")

print("---------list-----------")
n1 = [1, 2.1, True, "hello", 5j]
print(f"n1={n1} typeof(n1)={type(n1)}")

print("---------set-----------")
n1 = {1, 2.1, True, "hello", 5j}
print(f"n1={n1} typeof(n1)={type(n1)}")

print("---------dict {k:v,k:v,k:v}-----------")
n1 = {1: "komal", 2.1: 1000}
print(f"n1={n1} typeof(n1)={type(n1)}")
n2 = {}
print(f"n2={n2} typeof(n2)={type(n2)}")