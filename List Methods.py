# List Methods:
# List.sort()
# This method sorts the list in ascending order. The orginal list is updated
# Example1:
colors=["voilet","indigo","blue","green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,8,9,7]
num.sort()
print(num)

# Examples:
colors = ["violet","indigo","Blue","Green"]
colors.sort(reverse=True)
print(colors)

# reverse():
# This method reverse the order of the list 
# Example:
colors=["voilet","indigo","blue","green"]
colors.reverse()
print(colors)

num=[4,2,5,3,6,1,2,1,2,8,9,7]

# Example3:
colors = ["voilet","indigo","blue","green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
# The reverse Parameter is set to False by default
# Note: Do not Mistake the reverse parameter with the reverse method

# reverse():
# This method  reverse the order of the list 
# Example1:
colors=["violet","indigo","blue","green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

# index():
# This method returns the index of the first occurance of the list item
# Example1:
colors = ["voilet","green","indigo","blue","green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))

# copy:
# Return copy of the list. This can be done to perform operator on the list without modifying the orginal list 
colors = ["voilet","green","indigo","blue"]
newlist = colors.copy()
print(colors)
print(newlist)

# append():
# Returns copy of the list. This can be done to perform operations on the list without modifying the orginal list. 
# Examples1:
colors = ["voilet","indigo","blue"]
colors.append("green")
colors.append("Black")
print(colors)

# insert():
# The method inserts an item at the given index user has to specify index and the system to be inserted with in the insert() method 
# Example1:
colors = ["voilet","indigo","blue"]
print(colors)

# extend():
# This method adds an entire list or any other collection datatype (sets, tuple, dictionary) to the existing list. 
# Example1:
# add alist to a list
colors = ["voilet","indigo","blue"]
rainbow = ["green","yellow","orange","red"]
colors.extend(rainbow)
print(colors)

# concating two list:
# you can simply concatenate two list to join two list 
# Example1:
colors = ["voilet","indigo","blue","green"]
colors2 = ["yellow","orage","red"]
print(colors+colors2)

# Programm:
L = [11,45,1,2,4,6]
print(L)
L.append(7)
L.sort(reverse=True)
L.reverse()
print(L.index(1))
print(L.count(1))

# m = L.copy()
# m[0] = 0
# L.insert(1.899)
# m = [900,1000,1100]
# k=L+m
# print(k)