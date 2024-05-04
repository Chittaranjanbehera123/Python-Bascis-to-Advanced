# break=terminates loop

for i in range(1, 6):
    if i == 3:
        print(i)
        break
        print("work stopped")
    else:
        print(i)

print("work completed")

# continue-continues from next iteration but it ignores the next step

for i in range(1, 6):
    if i == 3:
        # print(i)
        continue
        print(i)
        print("work stopped")
    else:
        print(i)

print("work completed")

# pass-pass from next iteration also execute next step
# used to write empty block

for i in range(1, 6):
    if i == 3:
        # print(i)
        pass
        print(i)
        print("work stopped")
    else:
        print(i)

print("work completed")

# for i in range(5):
#     pass

# if True:
#     pass


# While loop


while True:
    n = int(input("enter number="))
    if n == 11:
        print("you win")
        break
    else:
        print("keep trying")

i = 1
while i <= 5:
    print(i)
    if i == 3:
        # break
        # continue
        pass
    i = i + 1

j = 1
while j <= 10:
    if j == 5:
        pass
        # j = j + 1
    else:
        print(j)
        j = j + 1
print("outside while")