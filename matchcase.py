# WAP to take 0 to 6 as day number and print respective dayname
# testcase-1if other than 0 to 6 
try:
    daynumber = int(input("Enter day number="))
    match daynumber:
        case 0:
            print(daynumber,"is sunday")
        case 1:
            print(daynumber,"is Monday")
        case 2:
            print(daynumber,"is Tuesday")
        case 3:
            print(daynumber,"is Wednessday")
        case 4:
            print(daynumber,"is Thrusday")
        case 5:
            print(daynumber,"is Friday")
        case 6:
            print(daynumber,"is satuerday")
        case _:
            print("Invalid day number")

except:
    print("Invalid input")