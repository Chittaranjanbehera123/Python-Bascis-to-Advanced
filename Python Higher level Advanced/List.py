# Example1:
myList = ["banana","Cherry","apple"]
print(myList)

for x in  myList:
    print(x)
    
if "apple" in myList:
    print("yes")
else:
    print("no")
    
print(len(myList))

myList.append("Lemon")
print(myList)


# Example2
myList = ["banana","Cherry","apple"]
print(myList)

Item=myList.pop()
print(Item)
print(myList)

# Example3
myList=[4,3,1,-1,-5,10]
print(myList)

myList.sort()
print(myList)

# Concatenate
# Example4
myList=[0] * 5
print(myList)

myList2=[1,2,3,4,5]
new_List=myList+myList2
print(new_List)

# Square
# Example5
myList=[1,2,3,4,5,6]
b=[y*y for y in myList]

print(myList)
print(b)