#LIST EXERCISE
#create a list of numbers and find sum,max,min(without buildin function)
num=[10,20,30,40,50]
total=0
for x in num:
    total+=x
maximum=num[0]
minimum=num[0]
for x in num:
    if x>maximum:
        maximum=x
    if x<minimum:
        minimum=x
print("sum :",total)
print("max :",maximum)
print("min :",minimum)

#write a program to remove the duplicate from a list
num=[2,2,4,4,6,6,8,8,10,10]
unique=[]
for x in num:
    if x not in unique:
        unique.append(x)
print("unique list:",unique)

#Rotate a list by k positions
num=[1,2,3,4,5]
k=3
rotated=num[k:]+num[:k]
print(rotated)

#Find the  second largest element in a list
num=[30,45,78,90,70]
largest=max(num)
num.remove(largest)
second_largest=max(num)
print("second largest num is:",second_largest)

#merge two sorted list into a single sorted list(without using sort())
list1=[1,3,5]
list2=[2,4,6]
i,j=0,0
merged=[]
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        merged.append(list1[i])
        i+=1
    else:
        merged.append(list2[j])
        j+=1
merged+=list1[i:]
merged+=list2[j:]
print(merged)

#TUPLE EXERSICE
#write a program to find repeated items in a tuple
t=(1,2,3,1,2,3,1,2,3)
repeated=[]
for i in t:
    if(t.count(i)>1 and i not in repeated):
       repeated.append(i)
print(repeated)

##convert a list of tuples into dictionary
list_of_tuples=[("a",1),("b",2)]
d=dict(list_of_tuples)
print(d)


##given a tuple of numbers,find the element wise sum of two tuples
t1=(1,2,3)
t2=(4,5,6)
result=[]
for i in range(len(t1)):
    result.append(t1[i]+t2[i])
print(tuple(result))

##check whether all elements in a tuple are the same        
tuple=(6,6,6,6)
if(len(tuple)==4):
    print("all elements are same")
else:
    print("not same")

##find the index of given element in a tuple
tuple=(2,4,6,8,10)
index_value=tuple.index(6)
print(index_value)

##DICTIONARY
count the frequency of words in a sentence using dictionary
sentence = "hello world hello python world"
words = sentence.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

##merge two dictionary into one (without using update())
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = {**d1, **d2}
print(merged)

##write a program to find the key with the maximum value in a dictinary
d = {"a": 10, "b": 25, "c": 15}
max_key = max(d, key=d.get)
print(max_key)

##sort a dictionary by its value
d = {"a": 3, "b": 1, "c": 2}
sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_dict)

##invert a dictionary
d = {"a": 1, "b": 2}
inverted = {v: k for k, v in d.items()}
print(inverted)


















































