# if 
a = int(input("Enter your age:"))
print("Your age is:", a)

if(a>18):
    print("You can drive")
    print("yes")
    print("yeah")

else:
    print("you cannot drive")
    print("No")
    print("Yeah")

# elif.py 
# Example
num = int(input("Enter the value of num:"))
if(num<0):
    print("Number is negative")
elif(num==0):
    print("Number is Zero")
else:
    print("Number is possitive")

# Example:2
num = int(input("Enter the value of num:"))
if(num<0):
    print("Number is negative")
elif(num==0):
    print("Number is Zero")
elif(num == 999):
    print("Number is Special.")
else:
    print("Number is possitive")
    print("I am happy now")