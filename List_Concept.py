#Create a list of numbers from 1 to 5 and print the third element
li=[1,2,3,4,5]
print(li[2])

#Add the number 10 to the end of the list
num=[10,20,30,40,50]
num.append(10)
print(num)

#Replace the second item in a list with the value of 99
li=[50,60,70,80,100]
li[1]=99
print(li)

#remove the number 3 from the list[1,2,3,4,5]
li=[1,2,3,4,5]
li.pop(2)
print(li)

#Print the length of the list[4,5,6,7]
num=[4,5,6,7]
print(len(num))

#Create a list of 3 fruits and print the first one
li=['apple','strawberry','kiwi']
print(li[0])

#Print the last element of the list[10,20,30,40,50]using negative indexing
num=[10,20,30,40,50]
print(num[-1])

#Combine two list[1,2] and [3,4]
list1=[1,2]
list2=[3,4]
combined=list1+list2
print(combined)

#check if the number exists in the list[5,6,7,8]
numbers=[5,6,7,8]
if(7 in numbers):
    print("7 exists in the list")
else:
    print("7 doesn't exists in the list")

#Print all items in the list[100,200,300]using a for loop
items=[100,200,300]
for x in items:
    print(x)


