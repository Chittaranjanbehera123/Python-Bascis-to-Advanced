mytuple=tuple(["Max", 28, "Boston"])
print(mytuple)


if "Tim" in mytuple:
    print("yes")
    
else:
    print("no")
    
# Example2
my_tuple=('a','p','p','l','e')
print(my_tuple.index('a'))

my_list=list(my_tuple)
print(my_list)

my_tuple2=tuple(my_list)
print(my_tuple2)


# Example: Demonstrating List and Tuple Unpacking
# List Unpacking
my_list = ['o', 'r', 'a', 'n', 'g', 'e']
o, r, a, n, g, e = my_list
print(o, r, a, n, g, e)  # Prints: o r a n g e

# Tuple Unpacking
my_tuple = ('b', 'a', 'n', 'a', 'n', 'a')
fruit1, fruit2, fruit3, fruit4, fruit5, fruit6 = my_tuple
print(fruit1, fruit2, fruit3, fruit4, fruit5, fruit6)  # Prints: b a n a n a