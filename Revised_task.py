#BASIC LOGIC & DATA TYPE[1-10]
print("hello world")
#SWAP TWO VARIABLE
a=int(input("enter the number:"))
b=int(input("enter the number:"))
print(f"before swap:a={a},b={b}")
a,b=b,a
print(f"after swap:a={a},b={b}")
#CHECK IF THE NUMBER IS EVEN OR ODD
num=int(input("enter the number:"))
if(num%2==0):
    print("num is even")
else:
    print("num is odd")
#CHECK IF THE NUMBER IS +VE,-VE,OR ZERO
x=int(input("enter the number:"))
if(x>0):
    print("x is +ve")
elif(x<0):
    print("x is -ve")
else:
    print("x is zero")
#FIND THE MAXIMUM OF THREE NUMBERS
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if(a>=b and a>=c):
    print("a is maximum num")
elif(b>=a and b>=c):
    print("b is maximum num")
elif(c>=a and c>=b):
    print("c is maximum num")
else:
    print("invalid")
    
#SUM OF DIGITS OF NUMBERS
n=int(input("enter the number:"))
s=0
while(n>0):
    s+=n%10
    n//=10
print(s)
#CHECK IF THE YEAR IS A LEAP YEAR
year=int(input("enter the number:"))
if(year%400==0):
    print("it is leap year")
else:
    print("it is not leap year")
#CHECK IF THE CHAR IS VOWEL OR CONSONENT
str="harshaa"
str=str.lower()
vowel=0
consonent=0
vowel_set="aeiou"
for char in str:
    if char.isalpha():
        if char in vowel_set:
            vowel+=1
        else:
            consonent+=1
print("no.of.vowels:",vowel)
print("no.of.consonents:",consonent)
#CALCULATE THE FACTORAIL OF NUMBER
n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)



#[STRINGS AND LOOP]
#CHECK IF A STRING PALINDROME
string="ramar"
string=string.replace(" ","").lower()
if(string==string[::-1]):
   print("palindrome")
else:
    print("not palindrome")
#COUNT VOWELS & CONSONENTS IN A STRING
string="vetrivel"
string=string.lower()
vowel=0
consonent=0
vowel_set="aeiou"
for ch in string:
    if string.isalpha():
        if ch in vowel_set:
            vowel+=1
        else:
            consonent+=1
print("no.of.vowels:",vowel)
print("no.of.consonents:",consonent)
#REMOVE ALL VOWELS IN A STRING
x="chettinad"
vowels="aeiouAEIOU"
res=" "
for ch in x:
    if ch not in vowels:
        res+=ch
print(res)
#COUNT FREQUENCY OF CHARACTERS IN A STRING
z="megavarshana"
freq={}
for ch in z:
    if ch!=" ":
        ch=ch.lower()
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
for key,value in freq.items():
    print(f"{key}:{value}")
#REVERSE A STRING
z="vetrivel"
rev=" "
for i in range(len(z)-1,-1,-1):
    rev+=z[i]
print(rev)


#LIST&TUPLES
#find the largest elements in a list
li=[22,33,44,55,66]
largest=li[0]
for num in li:
    if(num>largest):
        largest=num
print(num)
#remove duplicate from a list
f=[1,2,2,2,3,4,4,6,6]
unique=[]
for num in f:
    if(num not in unique):
        unique.append(num)
print(unique)
#sort a list without using build in sort()
a=[3,5,2,1]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
    print(a)
#check if a list is sorted
num=[9,8,7,6,5]
print(num == sorted(num))
#find the second largest number in a list
li=[15,67,89,56,44]
x=li[2]
print(x)



#DICTIONARIES & SETS
#count word frequency in a sentence using a dictionary
sentence="this is a test this is only a test"
words=sentence.split()
freq={}
for i in words:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
#merge two dictionaries
stu1={1:'harsha',2:'varshaa',3:'dhananya'}
stu2={4:'saniya',5:'karthiga',6:'lalala'}
stu1.update(stu2)
print(stu1)
#check if two sets have common elements
set1={1,2,3}
set2={4,5,6}
print(bool(set1&set2))
#remove a key from dictionary
my_dict={'a':10,'b':20,'c':30}
del my_dict['b']
print(my_dict)


#FUNCTIONS,LOOPS AND LOGIC
#check if number is prime
num = int(input("enter the number:"))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
#generate fibonaaci sequence up to n terms
n = 10
a, b = 0, 1 
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#print all prime numbers in a range
start = 10
end = 50
print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if num > 1:  # Only numbers greater than 1 can be prime
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
#create a number guessing game
secret=6
guess=0
while(secret!=guess):
    guess=int(input("enter the num:"))
    if(secret==guess):
        print("grant access")
    else:
        print("try again")






































    






















