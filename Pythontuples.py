# Python Tuples
# Tuples are orderd collection of data items. They store Multiple items in a single variable . Tuple items are separated by commas and enclosed within round brackets 0 Tuples are unchangeble Meaning we can not alter them after creation
# Example1:
tuple1 = (1,2,3,5,4,6)
tuple2 = ("Red","Green","Blue")
print(tuple1)
print(tuple2)

# Example2:
details = ("Abhijit",18,"FyBscII",9.8)
print(details)

# Programm1:
tup = (1,2,76,342,32,"green",True)
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])

if 3421 in tup:
    print("yes is Present in this tuple")
tup2 = tup[1:4]
print(tup2)

# Manipulating Tuples:
# Tuples are immutable, hence if you want to add remove  of change tuple items, then first you must convert the tuple to list. Perform Operations on that list and convert it back to tuple
# Example1:
countries = ("spain","Italy","India","England","Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# Exercise2:
# Good Morning sir 
import time
3
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

# Alternatively, you can use the following line to get the hour from user input
hour = int(input("Enter hour:"))
print(hour)
if(hour>=0 and hour<12):
    print("Good Morning sir!")
elif(hour>=12 and hour<17):
    print("Good Afternoon sir!")
elif(hour>=17 and hour<0):
    print("Good Night Sir!")