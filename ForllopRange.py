# Example1:
print(range(10))
print(type(range(10)))
print(type(range))
print(list(range(10)))
print(tuple(range(10)))
print(set(range(10)))

# Example2:
print("even numbers=", list(range(2, 11, 2))) #[2,4,6,8,10]
print("even odd=", list(range(2, 11, 3))) #[2,5,8]
print("even numbers=", list(range(2, 11)))
print("odd numbers=", list(range(1, 11, 2))) #[1,3,5,7,9]

print(list(range(5)))  # [0,1,2,3,4]
print(list(range(-5)))  # []
print(list(range(1, 0)))  # deafult steps=+1 []
print(list(range(1, 0, -1)))  # [1]
print(list(range(4, 0, -1)))  # [4, 3, 2, 1]
print(list(range(-5, 0, -1)))  # []
print(list(range(-5, 0, +1)))  # [-5,-4,-3,-2,-1]
print(list(range(-5, 0)))  # [-5,-4,-3,-2,-1]
print(list(range(-5)))  # []
print(list(range(-5, -1)))  # [-5,-4,-3,-2]
print(list(range(-5, -2)))
print(list(range(1, -5)))  # []
print(list(range(int(8.4)))) # [0, 1, 2, 3, 4, 5, 6, 7]
# print(list(range(8.4))) #typeerror
print(list(range(-10, 0, -3)))  # []
print(list(range(10, 0, -3)))  # [10,7,4,1]
print(list(range(0, -5, -1)))  # [0,-1,-2,-3,-4]
print(list(range(0, -5, -2)))  # [0,-2,-4]
print(list(range(-1, -5, -1)))  # [-1,-2,-3,-4]
print(list(range(-1, -5, -2))) #  [-1,-3]

# Example3:
n=int(input("Enter your Number:"))
for i in range(11):
    if(i==0):
        print("skip the iteration")
        continue
    print("5x",i,"=",5*i)

# Example:4
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
     break

# Example5:
msg = "welcome to python world"
for i in msg:
    print(i)

msg = "welcome to python world"
for i in msg:
    print(msg)

msg = ["e", "welcome to python world"]
for i in msg:
    if i == "e":
        break
    else:
        print(i)

# Example6:
# WAP to show fibboncci series for range by using for loop
# The sum of Previous two numbers is the Current number
try:
    n = int(input("enter range for series="))
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(1, n-1):
        c = a + b
        print(c)
        a = b
        b = c

except:
    print("invalid input")

