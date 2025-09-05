##MULIPLICATION TABLE
x=int(input("enter the number:"))
print(f"\n multiplication of {x}")
for i in range(1,11,1):
    print(f"{x}x{i}={x*i}")

##SUM OF N NATURAL NUMBER
n=int(input("enter the number:"))
total=0
for i in range(1,n+1):
    total+=i
    print(f"the sum of {n} natural number is:{total}")

##FACTORIAL CALCULATOR
num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact*=i
    print(f"the factorial of {num} is:{fact}")

##COUNTDOWN TIMER
num=int(input("enter the number:"))
print(f"countdown from {num} to 1")
for i in range(num,0,-1):
    print(i)
print("liftoff")

##REVERSE A NUMBER
num=input("enter the number:")
reverse=' '
for i in range((len(num)-1),-1,-1):
    reverse+=num[i]
    print(f"reverse number is,{reverse}")

##PRINT EVEN NUMBER BETWEEN 1 AND 100
i=2
while(i<=100):
    print(i,end=" ")
    i+=2

##SUM OF DIGITS
n=int(input("enter the number:"))
s=0
while(n>0):
    s+=n%10
    n//=10
print(s)

##NUMBER GUESSING NAME
secret=7
guess=0
while(guess!=secret):
    guess=int(input("enter the number:"))
    if(guess==secret):
        print("correct! you guessed it")
    else:
        print("try again.")

##CHECK FOR PRIME NUMBER
num=int(input("enter the number:"))
for i in range(2,num):
    if(num%1==0):
        print("not prime")
        break
else:
    print("prime")

##SQUARE HOLLOW PATTERN
for i in range(1,6,1):
    for j in range(1,6,1):
        if(i==1 or j==5 or i==5 or j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    


