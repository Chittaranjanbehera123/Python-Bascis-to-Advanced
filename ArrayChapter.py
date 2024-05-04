# Creating an array (list)
Chintu_array = [1, 2, 3, 4, 5]

# Printing the original array
print("Original array:", Chintu_array)

# Modifying elements in the array
Chintu_array[0] = 10
Chintu_array[2] = 30

# Printing the modified array
print("Modified array:", Chintu_array)


# Example2:
# Taking input for the number of elements in the array
# Write a Program input ten number and point them in a reverse order. 
# reversing 10 numbers entered by user
num = int(input("enter count for numbers="))
numberslist = []
for i in range(num):
    number = int(input(f"enter {i} number="))
    numberslist.append(number)

print(numberslist)
for i in numberslist:
    print(i)

print("reverse order")
for i in numberslist[::-1]:
    print(i)

# Example3:
num = {10, 15, 20, 25, 30, 69, 70, 45, 67}
numberslist = []
for i in (num):
    number = int(input(f"Enter {i} number: "))
    numberslist.append(number)

print("Numbers List:", numberslist)
print("Reverse Order:")
for i in reversed(numberslist):
    print(i)