# Example1:
print("Welcome")
print(4 + 5)
a = 676
b = 65
a = 10
print(a + b)
x = int(input("enter any integer number="))
y = int(input("enter any integer number="))
print(x + y)

# varibles(identifiers which is used to store some value)
# Rules
# 1)cannot start variables names with digit or special character except underscore(_)
_ = 3423
print(_)
_______ = 23434
print(_______)
# 1name="welcome"  #error

# 2)whitespace is not allowed
# roll no=234 #invalid
roll_no = 343

# 3)keywords are not allowed
# True="dgdfg"   #error
# if=4534       #error

# 4) if value has character or special character then represent in quotes
# 5) variablename must have value


# Example2:
# name = rahul #error
name = "rahul"
emailid = "rahul@gmail.com"
# password=24343@#$%  #error
password = "24343@#$%"
x = int(1e1)
print(x)
python_features = """high-level
dynamic
interpretive
easy"""
print(python_features)
numbers = 56 + 45 - 56 * 34 - 90
print(numbers)

# multi-valued variables
names = "raj", "komal", "faiz"
print(names)
numbers = 1, 2, 3
print(numbers)
# name, rollno = "komal,12" error
name, rollno = "komal", 12
print(name)
print(rollno)

# Big numbers
price = 232342_234234_23424_234234_23423423_2423432
print(price)
