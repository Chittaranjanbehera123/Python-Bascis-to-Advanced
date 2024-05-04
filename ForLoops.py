# Example1:
name='Chittaranjan'
for i in name:
    print(i,end=",")
print()

# Example2:
colors =["Red","Green","Blue","Yellow"]
for x in colors:
    print(x)

# Example3:
for k in range(5):
    print(k)

# Example4:
name='Chittaranjan'
for i in name:
    print(i)
    if(i=="b"):
        print("The Something is Special!")

colors =["red","Green","Blue","Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k+1)

# for k in range(1,120001):
#     print(k)

for k in range(1,12,3):#[Dout]
    print(k)

# Example2:
count=5
while(count>0):
    print(count)
    count=count-1

# Example3:
i=int(input("Enter the number:"))
while(i<=38):
    print(i)
    
    print("Done with the loop")

count=5
while(count>0):
    print(count)
    count = count-1
else:
    print("Iam Inside else")

# Example4:
for i in range(1,101,1):
    print(i,end="")
    if(i==50):
        break
    else:
        print("Mississippi")
        print("Thank you")