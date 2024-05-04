# Python Function:
# Ans: A function  is a block of code that Performs a specific task  whenever it is called. In Bigger Programms where we have large amounts of code , it is a dvisable to create or use existing function that make the Programm flow organized and neat.
# calling function:
# Example1:
def name(firstname, lastname):
    print("Hello", firstname, lastname)

name("Chittaranjan", "Behera")

# Default Arguments
# Example3:
def name(fname, mname="RANJAN", lname="BEHERA"):
    print("Hello", fname, mname, lname)

name("CHITTARANJAN")

# Keyword arguments:
# Example4:
def name(fname, mname, lname):
    print("Hello",fname,mname,lname)

name(mname="Ranjan",lname="Behera",fname="Chittaranjan")

# Required arguments:
# Example5:
# def name(fname,mname,lname):
#     print("Hello",fname,mname,lname)

# name("Chittaranjan","Behera")

# Example6:
# Variable-length arguments:
# There are two types of Arguments:
# 1.Arbitary Arguments
# 2.Keyword Arbitary Arguments
def name(*name):
    print("Hello",name[0],name[1],name[2])

name("Chitta","Ranjan","Behera")

# 2.
def name(**name):
    print("Hello",name["fname"],name["mname"],name["lname"])

name(mname="Kumar",lname="Behera",fname="Ashok")


# Return Statement:
# Ans: The return Statement is used to return the value of the expression back to the calling function. 
# Example7:
def name(fname,mname,lname):
    return "Hello"+fname+" "+mname+" "+lname
print(name("james","Bachana","Barnes"))

# Example8:
def calculate_average(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum / len(numbers)

# Example calls
result = calculate_average(4, 6)
print("Average:", result)

result = calculate_average(5, 6, 7, 1)
print("Average:", result)

# Example9:
animals = ["cat", "dog", "Mouse", "Pig", "horse", "donkey", "goat", "cow"]

# Print a slice from index 3 to 6 (7 is exclusive)
print(animals[3:7])

# Print a slice using negative indexing
print(animals[-7:2])