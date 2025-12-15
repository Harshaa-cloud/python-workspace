##LIST COMPREHENSION
#Create a list of squares of all even numbers between 1 and 20
squr=[x*x for x in range(1,21) if(x%2==0)]
print(squr)
#From a list of words, return a new list containing only words with more than 4 letters.
li=["apple","mango","grapes","dog","cat"]
res=[word for word in li if(len(li)>4)]
print(res)
#Convert a list of Celsius temperatures to Fahrenheit using list comprehension.
celsius=[0,10,20,30]
fahrenheit=[(c*9/5)+32 for c in celsius]
print(fahrenheit)


##MAP()FUNCTIONS
#Use map() and lambda to get cubes of numbers from 1 to 10.
num=range(1,11)
cubes=list(map(lambda x:x**3,num))
print(cubes)
#Use map() to convert all strings in a list to uppercase.
word=["apple","mango","grapes"]
res=list(map(lambda x:x.upper(),word))
print(res)
#Use map() to create a list containing the lengths of each word in a given list.
li=["apple","mango","grapes"]
res=list(map(len,li))
print(res)


##FILTER()
#Use filter() and lambda to extract even numbers from a list.
num=[1,2,3,4,5]
res=list(filter(lambda x:x%2==0,num))
print(res)
#Use filter() to get only the words that start with the letter ‘A’ or ‘a’.
word=["apple","orange","ant","angrybird"]
res=list(filter(lambda x:x[0] in ['A','a'],word))
print(res)
#Use filter() to remove all negative numbers from a list.
numbers = [5, -2, 0, -7, 8, -1, 3]
positive_numbers = list(filter(lambda x: x >= 0, numbers))
print(positive_numbers)


##REDUCE()
#Use reduce() and lambda to find the sum of all numbers in a list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)
#Use reduce() and lambda to find the maximum value in a list.
from functools import reduce
numbers = [10, 25, 5, 70, 30]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)
#Use reduce() to compute the product of all numbers in a list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)
print(product)




