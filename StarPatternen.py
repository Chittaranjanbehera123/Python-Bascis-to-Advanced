# Example1:
row=int(input("Enter Your Rows:"))
for i in range(1, row):
    for j in range(1,i+1):
        print(" * ",end="")
    print()

print("Next Line:")
# Example2:
for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print("*", end=" ")
    print()

print("Next Line:")
# Example4:
row = int(input("Enter Your Rows: "))
for i in range(1, row + 1):
    for j in range(1, row + 1):
        if (i + j) <= row:
            print(" ", end="")
        else:
            print("*", end="")
    print()

# Example5:
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")

    for k in range(2 * i - 1):
        print("*", end=" ")

    print()

