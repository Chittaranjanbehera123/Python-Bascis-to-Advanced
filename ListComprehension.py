# Example1:
# Accepts items with the small letter "0" in the new list 
names = ["Milo","Sarah","Baruno","Anastasia","Rosa"]
nameswith_0=[item for item in names if "0" in item]
print(nameswith_0)

# Example2:
marks=[3,5,6, "Chintu",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5])

print(marks[-3]) #negative index
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Possitive index
# print[marks[2]] # possitive index

if "chintu" in marks:
    print("yes")
else:
    print("No")

if "6" in marks:
    print("yes")
else:
    print("No")

# same thing applies for string as well!!
    if "ch" in "chintu":
        print("yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])
