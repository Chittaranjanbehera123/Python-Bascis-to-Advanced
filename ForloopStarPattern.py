# Example1:


print("(horizontal)row-wise printing")
for i in range(1, 6):
    print("*", end="")

print("\n(vertical)column-wise printing")
for i in range(1, 6):
    print("*")

print("2-D printing for row and column are same")
for i in range(1, 6):
    print("*" * 10)


row = int(input("enter row count="))
column = int(input("enter column count="))
for i in range(row):
    for j in range(column):
        # print("*", end="")
        # print(i, end="")
        # print(j, end="")
        print(i * j, end=" ")
    print()


for i in range(1, row + 1):
    for j in range(1, column + 1):
        print(i * j, end="\t")
    print()


for i in range(1, row + 1):
    for j in range(1, column + 1):
        print(f"{i},{j}", end="\t")
    print()

print("Left incremental triangle")
row = int(input("enter row count="))
for i in range(1,row):
    for j in range(1,i + 1):
        print("*", end=" ")
    print()

print("Left decremental triangle")
row = int(input("enter row count="))
for i in range(row, 0, -1):
    for j in range(i - 1):
        print("*", end=" ")
    print()


print("Right incremental triangle-----------")
row = int(input("enter row count="))
for i in range(row):
    for j in range(i, row - 1):
        print(" ", end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    print()

print("Right decremental triangle-----------")
row = int(input("enter row count="))
for i in range(row):
    for j in range(i):
        print(" ", end=" ")
    for k in range(i, row):
        print("*", end=" ")
    print()


print("Pyramid(Hill incremental)-----------")
row = int(input("enter row count="))
for i in range(row):
    for j in range(1, row - i):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end=" ")
    print()


print("Pyramid(Hill decremental)-----------")
row = int(input("enter row count="))
for i in range(row, 0, -1):
    for j in range(row, i, -1):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()