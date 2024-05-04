# Python Dictionaries:
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key value pairs that are Separated by commas and enclosed within curly brackets :
# Example1:
info = {'name':'Chittaranjan', 'age':23, 'eligible':True}
print(info)

# Accessing Dictionary items:
# Example1:
info = {'name':'Chittaranjan','age':19,'elgible':True}
print(info['name'])
print(info.get('elgible'))

# Accessing Multiple Values: 
# we can print all the values in the in the dictionary using values Method .
# Example2:
info = {'name':'Chittaranjan','age':23,'elgible':True}
print(info.values())

# Accessing Keys: 
# We can Print all the keys in the dictionary using keys() Method. 
info = {'name':'Chittaranjan','age':23,'elgible':True}
print(info.keys())

# Accessing Key-value Pairs: 
# We can Print all the key-value pairs in the dictionaries using items() Method 
# Example2:
info = {'name':'Chittaranjan','age':23,'elgible':True}
print(info.items())

# Programm:
info = {'name':'Chittaranjan','age':23,'elgible':True}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The values Corresponding to the key {key} is {info[key]}")

    print(info.items())

    for key, value in info.items():
        print(f"The value corresponding to the key {key} is {value}")

# Dictionary Methods: 
# Dictionary use several built-in methods for manipulating They are listed below 
# Update():
info = {'name':'Chittaranjan','age':19,'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)