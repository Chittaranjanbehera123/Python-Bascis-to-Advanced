# Example1:
i=5
while(i>0):
    print("Hello")
    i=i-1

# Example2:
i=5
while(i>=1):
    print("Hello Chintu")
    i=i-1

# Example3:
    # i=5
    # while(i<=10):
    #     print("Hello")

# Example4:
a=10.0
while(a<=10.5):
    print("Raindrops on roses...")
    a=a+0.1

# Example5:
i=1
while(i<=10):
    print(f"The value of:{i}")
    # i=i+1
    i+=1

# Example6:
x =1.1
while(x==1.1):
    x=x-0.1
    print(f"The value of:{x=}")

# Example7:
# write a program to input anumber and find out the sum of given?
# (123 = 1+2+3=6) sum =0
#   Q=123/10=12
    # r=123%10=3
    # 12/10=1
    # 12%10=2
    # 1/10=0
    # 1%10=1
sum = 0
n = int(input("Enter a Number:"))

while n > 0:
    r = n % 10
    sum = sum + r
    n = n // 10

print(f"The sum of Digits is: {sum}")

# Example8:
# WAP in 'c' to input a number and find out the reverse of a number
sum = 0
n = int(input("Enter a Number:"))

while n > 0:
    r = n % 10
    sum = sum*10 + r
    n = n // 10

print(f"The sum of Digits is: {sum}")

# Example9:
# WAP in c to input a no and check wheather it is Palindrom or not?
# Ans:"PALINDROM" if the reverse of a number is the orginal no.then it is called Palindrom
num = int(input("Enter a number:"))
m= n
sum = 0

while num > 0:
    r = n % 10
    sum = sum * 10 + r
    num = num // 10

if m == n:
    print("PALINDROME")
else:
    print("Not PALINDROME")

# Example10:
# WAP to input a number and check wheather a number is amstrong or not?
num = int(input("Enter a number:"))
m = n
sum = 0

while num > 0:
    r = n % 10
    sum = sum + r*r*r
    num = num // 10

if m == n:
    print("AMSTRONG")
else:
    print("Not AMSTRONG")

# Example11:
# write aprogram to determine wheather a number is Prime or not. A prime number is one which is divisible only by 1 or itself 
num=int(input("Enter a Number:"))
i=2
while(i<=num-1):
    if(num%i==0):
        print("Not a Prime number")
        break
    i+=1
    if(i==num):
        print("Prime Number")
    

# Example12:
num = int(input("Enter a number: "))

# if num > 1:
for i in range(2, num-1):
    if num % i == 0:
        print(num, "is not a prime number")
        break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")