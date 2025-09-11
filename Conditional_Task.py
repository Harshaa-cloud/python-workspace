#EVEN OR ODD
num=int(input("enter the number:"))
if(num%2==0):
    print(num, "is even")
else:
    print(num, "is odd")

#POSITIVE,NEGATIVE OR ZERO
x=int(input("enter the number:"))
if(x>0):
    print("num is +ve")
elif(x<0):
    print("num is -ve")
else:
    print("num is zero")

#LEAP YEAR CHECKER
year=int(input("enter the year:"))
if(year%400==0):
    print("it is leap year")
else:
    print("it is not a leap year")

#GRADE EVALUATOR
grade=int(input("enter the grade:"))
if(grade>=90 and grade<=100):
    print("Grade A")
elif(grade>=80 and grade<=89):
    print("Grade B")
elif(grade>=70 and grade<=79):
    print("Grade C")
elif(grade>=60 and grade<=69):
    print("Grade D")
else:
    print("Grade F")

#VOTING ELLIGIBILITY
age=int(input("enter the age:"))
if(age >=18):
    print("eligible for vote")
else:
    print("not eligible for vote")

#CHECK LARGEST OF THREE NUMBERS
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if(a>=b and a>=c):
    print(a,"is the largest number")
elif(b>=a and b>=c):
    print(b,"is the largest number")
else:
    print(c,"is the largest number")

#PASSWORD VALIDATOR
correct_password ="Opensesame"
password=input("enter the password:")
if(password==correct_password):
    print("Access granted")
else:
    print("Access denied")

#DIVISIBILITY CHECKER
num=int(input("enter the number:"))
if(num%3==0 and num%5==0):
    print(num,"is divisible by both 3 and 5")
else:
    print(num,"is not divisible by both 3 and 5")

#CHECK THE DAY OF THE WEEK
day=int(input("enter the number(1-7):"))
if(day==1):
    print("monday")
elif(day==2):
    print("tuesday")
elif(day==3):
    print("wednesday")

    print("thursday")
elif(day==5):
    print("friday")
elif(day==6):
    print("saturday")
elif(day==7):
    print("sunday")
else:
    print("error:day out of range")

#NUMBER IN RANGE
x=int(input("enter the number:"))
if(10<=x<=20):
      print(x,"within the range of 10 to 20")
else:
    print(x,"out of range")

    



