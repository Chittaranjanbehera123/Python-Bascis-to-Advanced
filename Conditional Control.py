# Membership operator (in, not in)
# works in string,list,tuple,dict,set,range()
msg = "hello python"
print("h" in msg)
print("x" in msg)
print("123" in msg)
numbers = 332423
# print(3 in numbers)  # int can't be iterable
numbers = 23, 34, 56, 4, 3
print(numbers)
print(type(numbers))
print(3 in numbers)
print("343" not in msg)
print("" in msg)  # true
print(type(""))  # str
print(bool(""))
print(not (""))  # true


# # Identity (is,is not)
a = 5
print("a=", id(a))
b = 6
print("b=", id(b))
c = a
print("c=", id(c))
z = 5
print("z=", id(z))
print(z is a)
print(c is a)
print(a is b)
m = "python"
print("m=", id(m))
n = "java"
print("n=", id(n))
l = m
print("l=", id(l))
print(l is m)  # true
print(m is n)  # false
print(n is l)  # false

print("-------tuple--------")
x = (1, 2, "hi")
print("x=", id(x))
y = (1, 2)
print("y=", id(y))
k = x
print("k=", id(k))
p = (1, 2)
print("p=", id(p))
print(x is y)  # false
print(y is k)  # false
print(x is k)  # true
print(p is y)  # true

# print("---------list----------")
x = [1, 2, "hi"]
print("x=", id(x))
y = [1, 2]
print("y=", id(y))
k = x
print("k=", id(k))
p = [1, 2]
print("p=", id(p))
print(x is y)  # false
print(y is k)  # false
print(x is k)  # true
print(p is y)  # false