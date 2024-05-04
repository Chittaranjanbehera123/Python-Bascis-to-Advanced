for i in [2,3,4,6,8,0]:
    if(i%2!=0):
        continue
    print(i)

# Example2:
for i in range(12):
    if(i==0):
        print("skip the iteration")
        continue
    print("5x",i,"=",5*i)
    
    i=0
    while True:
        print(i)
        i=i+1
        if(i%100==0):
            break

# Example3:
# Factorial of any +ve integer number
n=int(input("Enter Number="))
fact=1
i=1
while(i<=n):
    fact=fact*i
    i=i+1
    print(f"factorial of {n}={fact}")        