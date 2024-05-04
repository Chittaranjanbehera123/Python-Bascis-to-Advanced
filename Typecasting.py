# Data Type Converstion
# Implicit-Automatic does by interpreter
# Explicit-By user

# Implicit
a = 4
b = 4
a = a / b
print(a)
c=10
d=2
divide = (c%d)
print(divide)
# print(a / b)  # shows result in float
n = 7, 89, 9
print(n)  # shows result in tuple

# Explicit
print("-------int to all")
n = 123
print(type(n))
n_int = int(n)
print(f"type of {n_int}={type(n_int)}")
n_float = float(n)
print(f"type of {n_float}={type(n_float)}")
n_str = str(n)
print(f"type of {n_str}={type(n_str)}")
n_complex = complex(n)
print(f"type of {n_complex}={type(n_complex)}")
n_bool = bool(n)
print(f"type of {n_bool}={type(n_bool)}")

print("-------float to all")
n = 123.76767
print(type(n))
n_int = int(n)
print(f"type of {n_int}={type(n_int)}")
n_float = float(n)
print(f"type of {n_float}={type(n_float)}")
n_str = str(n)
print(f"type of {n_str}={type(n_str)}")
n_complex = complex(n)
print(f"type of {n_complex}={type(n_complex)}")
n_bool = bool(n)
print(f"type of {n_bool}={type(n_bool)}")

print("-------str to all")
n = "welcome"
print(type(n))
# n_int = int(n)   #Error
# print(f"type of {n_int}={type(n_int)}")
# n_float = float(n) #error
# print(f"type of {n_float}={type(n_float)}")
n_str = str(n)
print(f"type of {n_str}={type(n_str)}")
# n_complex = complex(n)  #error
# print(f"type of {n_complex}={type(n_complex)}")
n_bool = bool(n)
print(f"type of {n_bool}={type(n_bool)}")
n = bool("")
print(f"type of {n}={type(n)}")
n = bool(None)
print(f"type of {n}={type(n)}")


# print("-------complex to all")
# n = 6j + 6
# print(type(n))
# n_int = int(n) #error
# print(f"type of {n_int}={type(n_int)}")
# n_float = float(n) #error
# print(f"type of {n_float}={type(n_float)}")
# n_str = str(n)
# print(f"type of {n_str}={type(n_str)}")
# n_complex = complex(n)
# print(f"type of {n_complex}={type(n_complex)}")
# n_bool = bool(n)
# print(f"type of {n_bool}={type(n_bool)}")

print("-------Boolean to all")
n = False
print(type(n))
n_int = int(n)
print(f"type of {n_int}={type(n_int)}")
n_float = float(n)
print(f"type of {n_float}={type(n_float)}")
n_str = str(n)
print(f"type of {n_str}={type(n_str)}")
n_complex = complex(n)
print(f"type of {n_complex}={type(n_complex)}")
n_bool = bool(n)
print(f"type of {n_bool}={type(n_bool)}")