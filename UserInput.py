print("----------bool----------")
n1 = True
print(f"n1={n1} typeof(n1)={type(n1)}")
n1 = False
print(f"n1={n1} typeof(n1)={type(n1)}")

# Taking user Input python
a = input("Enter your name:")
print("My name is",a)

x = input("Enter first Number.")
y = input("Enter second Number.")
print(x+y)

print(int(x)+int(y))

# Type casting
# implicit conversion
a_int = 1
b_float = 1.0
c_sum = a_int+b_float
print(c_sum)
print(type(c_sum))