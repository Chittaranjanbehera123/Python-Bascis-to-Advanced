# Python sets:
# set are unordered collection of data items They store Multiple items in a single variable . set items are separated by commas and enclosed within curly brackets {} sets are unchangeble. Meaning you cannot Change items of the set once created. sets do not contain duplicate items
# Example:
info = {"carlo",19,False,5,9,19}
print(info)
# Accessing set items
# using a For loop 
# you can access items of set using afor loop 
# Examples:
info = {"carlo",19,False,5.9}
for item in info:
    print(item)

# programm:
S = {2,4,2,6}
print(S)

info = {"carlo",19,False,5.9,19}
print(info)

chintu = set()
print(type(chintu))

for value in info:
    print(value)

# Symetric_difference and Symmetric_difference_updates()
# The Symmetric_difference() and symmetric_difference_update() Methods Prints only items that are not Similar to both the sets. The Symmetric_difference_update() Method  updates into the existing set from another set. 
# Example1:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# Using symmetric_difference_update method
# The difference and difference_updates() Methods Prints only items that are only Present in the Orginal set and not in both the sets , The difference() Method returns a new set whereas difference_update() Method updates into the existing set from another set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"} 
cities.symmetric_difference_update(cities2)
print(cities)

# sets Methods:
# There are Several in-Built Methods. 
# is disjoint(): 
# The isdisjoint() Method checks it items of given set are present in another set. This methods returns false if items are present, else it returns True 
# Examples1:
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
print(cities.isdisjoint(cities3))

# issuperset():[dout]
# The issupset() Method checks if all the items of a Particular set are present in the orginal set. it returns True if all the items are Present it returns False. 
# Example1:
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"seoul","Kabul"}
print(cities.issuperset(cities2))
cities3 = {"seoul","madrid","kabul"}
print(cities.issuperset(cities2))

# issubset():
# The issubset() Method checks if all the items of the orginal set are present in the particular set. It returns True if all the items are present, else it returns false. 
# Example1:
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Delhi","Madrid"}
print(cities2.issubset(cities))

# add():
# If you want to add a single item to the set use the add() method 
# Example1:
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.add("America")
print(cities)

# remove()/discard():
# We can use remove() and discard() Method to remove items form list 
# Example1:
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.remove("Tokyo")
print(cities)

# Pop():
# This method removes the last item of the set but the catch is that we don't know which items gets Popped as sets are unordered . assign However you can access the popped item if you assign the pop() method to a variable 
# Examples1:
cities = {"Tokyo","Madrid","Berlin","Delhi"}
items = cities.pop()
print(cities)
print(items)

# del:
# del is not a method, rather it is a keyword which deletes the set entirely. 
# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# del cities
# print(cities)
# Ans: Name Error

# Clear():
# This method clears all items in the set and print an empty set. 
# Examples2:
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.clear()
print(cities)

# check if item exist:
# You can also check if an item exists in the set or not 
# Example2:
chintu = {"carlo",19,False,5.9}
if "carlo" in chintu:
    print("Carlo is Present")
else:
    print("Carlo is absent")