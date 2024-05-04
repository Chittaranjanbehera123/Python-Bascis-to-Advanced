# Slicing Operations
fruit = "Mango"
length = len(fruit)
print("Mango is a",length,"Letter word")

# String as an array
# A string is essentially Sequence of Character can access the elements of this array
P = "ApplePie"
print(P[:5])
print(P[6])#returns character at Specified index

# Slicing Example
P = "ApplePie"
print(P[:5]) # slicing FromStart
print(P[5:]) # Slicing till End
print(P[2:6]) # Slicing in between
print(P[-8:]) # Slicing using negative index

# Loops through a string:
# Strings are arrays and arrays areiterable. Thus we can through Strings
# Example
alphabets = "ABCDE"
for i in alphabets:
    print(i)

# Example1
# Example
alphabets = "ABCDEF"
for i in alphabets:
    print(alphabets)

# Example:
fruit = "Mango"
fruitslen = len(fruit)
print(fruitslen)
print(fruit[0:4])
print(fruit[1:4])
print(fruit[:5])
print(fruit[0:-3])
print(fruit[-3:-1])

# Upper()
# The upper method converts astring to uppercase.
# Example
String = "AbcDEfghIJ"
print(String.upper())

# Lower()
# The Lower() Method converts astring to 
String = "AbcDEfghIJ"
print(String.lower())

# Strip():
# The Strip() Method removes any white space befores and after the string 
String2 = "SilverSpoon"
print(String2.strip())

# rstrip():[Douts]
# The rstrip() removes any trainling characters, Examples 
# Str3 = "Hello!!!"
# print(Str3.rstring("!"))

# replace():
# The replace Method all occurances of a String with another String Examples
String3 = "SliverSpoon"
print(String3.replace("Sp","M"))

# Split():
# The split Methods Splits the given string at the Specified instance and returns the Specified String as list Items
string4 = "SliverSpoon"
print(string4.split(" ")) # Splits the string at the whiteSpace


# Capitalize():
# The captilize() method turns only the first character of the string to uppercase and the rest other character of the string are turned to lowercase .
# Example:
str1 = "hello"
CapStr1 = str1.capitalize()
print(CapStr1)
str2 = "helloWorld"
CapitalizeStr2 = str2.capitalize()
print(CapitalizeStr2)

# Center():
# The center Method aligns the string to the center as per the parameters given by the User 
str1 = "Welcome to the console!!!"
print(str1.center(50))

# Count
# The count() Method returns the number of times the given value is has occured within the given string 
Str2 = "ChittaranjanBehera"
CountStr = Str2.count("a")
print(CountStr)

# ends():
# The ends with Method Checks if the String ends with agiven value. If you then return True, else return False
# Example:
Str1 = "Welcome to the console!!!"
print(Str1.endswith("!!!"))

# find():
# The find() Method searches for the first occurances of the given values and retuens the index where it is present . It given value is absent from the string then return-1
# Example:
Str1 = "He's name is Dan. He is an honest man"
print(Str1.find("is"))

# Example:
Str1 = "He's name is Dan.He is an honest man."
print(str1.find("Daniel"))

# index():
# The index() Method searches for the first occurances the given value and returns the index where it is present. if given value is absent from the string then raise an exception 
# Example:
str1 = "He's name is Dan.Dan is an honest man"
print(str1.index("Dan"))

# Example2:
# str1 = "He's name is Dan. Dan is an honest man"
# print(str1.index("Daniel"))

# isalnum():
# The isalnum() Method returns True only if the entire String only consits of A-Z,a-z,0-9. if any other character of punctuations are present. then it returns false 
# Example:
str1 = "WelcomeToTheconsole"
print(str1.isalnum())

# isalpha():
# The isalnum() Method returns true only if the entire string only consits of A-Z,a-z, if any other characters or punctions of number(0-9) are present, then it returns false 
# Examples:
str4 = "welcome"
print(str4.isalpha())

# islower():
# The islower() Method returns True if all the characters in the string are lower case. else if returns false 
# Examples:
str1 = "hello world"
print(str1.islower())

# isPrintable():
# The isPrintable() Method returns true if all the values within the given string are printable, if not, then return false 
Str1 = "We wish you a Merry christmas"
print(str1.isprintable())

# isSpace():
# The isSpace() Method returns true only and only if the String contains white Spaces, else returns false 
# Examples:
str1 = "    " #using Spacebar
print(str1.isspace())
str2=""
print(str1.isspace())

# istitle():
# The istitle() returns true only if the first letter of each word of the string is capitalize, else it returns false. 
# Example:
str2 = "To kill a making bird"
print(str2.istitle())

# isUpper:
# Examples:
str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())

# Startswith():
# Examples:
str1 = "Python is Interpreted language"
print(str1.startswith("Python"))

# swapcase():
# Example:
str1 = "Python is aInterpreted language"
print(str1.swapcase())

# title():
# Examples:
str1 = "He's name is Dan  is an an honest man."
print(str1.title())

x = (1,2, "hi")
print("x=",id(x))
y = (1,2)
print("y=", id(y))
k =x
print("k=", id(k))
p=(1, 2)
print("p=", id(p))
print(x is y)
print(y is k)
print(x is k)
print(p is y)
