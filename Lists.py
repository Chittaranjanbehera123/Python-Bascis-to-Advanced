# Python Lists:
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# Lists items are separated by comma and enclosed  within square brackets[].
# Example1:
Lst1=[1,2,3,5,4,6]
Lst2=["Red","Green","Blue"]
print(Lst1)
print(Lst2)

# Examples2:
list1=[8,2.3,[-4.5],["apple","banana"]]
print(list1)

# Tuple:
# A tuple is an ordered collection of data with elements Separated by a comma and enclosed within parenthesis Tuples are immutable and can not be modified after creation
# Example1:
tuple1=(("parret","sparrow"),("Lion","Tiger"))
print(tuple1)

# Mapped data dict:
# dict: A dictionary is an unorederd collection of data containing a key value pair, The key: Value pairs are enclosed within curly brackets
# Example1:
dict1 = {"name":"sakshi","age":20,"canvote":True}
print(dict1)

# LIST INDEX:
# 1.Accessing List Items:
# 2. Possitive Indexing:
# Example1:
colors=["Red","Green","Blue","Yellow","Green"]
print(colors[2])
print(colors[4])
print(colors[0])

# Example: Printing all element from a given index till the end 
animals=["cat","dog","bat","mouse","pig","horse","donkey","goat","cow"]
print(animals[4:]) #using Possitive indexes
print(animals[:-4])

# Example: Printing alternative values:
animals=["cat","dog","bat","mouse","pig","horse","donkey","goat","cow"]
print(animals[::2])
print(animals[-8:-1:2])