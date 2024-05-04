n=int(input("Enter your Age:"))
# print("Enter your age:")
if(n>=18):
    print("She is elgible for vote")
else:
    print("She don't elgible for vote")

n=int(input("Enter your Number"))
if(n>0):
    print("Number is Positive")
    print("I am Happy Now")
elif(n==0):
    print("Number is Zero")
else:
    print("The Number is Negative")

# Example2:
def chintu1():
    print("This is case 1")

def chintu2():
    print("This is case 2")

def chintu3():
    print("This is case 3")

def default4():
    print("This is case 4")

def switch_case(chintu_value):
    switch_dictionary= {
        1: chintu1,
        2: chintu2,
        3: chintu3,
        4: default4
    }

    try:
        selecting_case = switch_dictionary[chintu_value]
    except KeyError:
        print("This case is not handled.")
        return

    # call the selected function 
    selecting_case()

switch_case(1)
switch_case(2)
switch_case(3)
switch_case(4) # This will invoke the default case
switch_case(5) # This will print "This case is not handled."