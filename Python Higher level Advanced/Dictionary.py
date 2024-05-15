# Example1:
mydict = {"name":"Max", "age":28, "City":"Newyork"}
print(mydict)


mydict["email"] = "97chittaranjanbehera@gmail.com"
print(mydict)

mydict.popitem()
print(mydict)

# Example 2
mydict = {"name": "Max", "age": 28, "City": "Newyork"}
print(mydict)

if "Lastname" in mydict:
    print(mydict["Lastname"])  # corrected key spelling

# Example 3
mydictitems = {"name": "Max", "age": 28, "City": "Newyork"}
print(mydictitems)

for key, value in mydictitems.items():  # use items() method to iterate over both keys and values
    print(key, value)

# Example4:
mydict = {"name": "Max", "age": 28, "City": "Newyork"}
print(mydict)

mydict_cpy = dict(mydict)

mydict_cpy = dict(mydict)
mydict_cpy["email"] = "97chittaranjanbehera@gmail.com"
print(mydict_cpy)
print(mydict)


# Example5:
my_dict={"name": "Max", "age": 28, "City": "Newyork", "email":"97chittaranjanbehera@gmail.com"}
my_dict_2=dict(name="Mary",age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)

# Example6:
my_dict={3: 9, 6:36, 9:81}
print(my_dict)

mytuple=[8,7]
mydict={mytuple:15}
print(mydict)