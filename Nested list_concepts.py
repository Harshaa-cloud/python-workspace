#Create a nested list with two sublist:[[1,2,3],[4,5,6]]
nested_list=[[1,2,3],[4,5,6]]
print(nested_list)

#Access the number 5 from the nested list[[1,2,3],[4,5,6]]
nested_list=[[1,2,3],[4,5,6]]
print(nested_list[1][2])

#Replace the number 2 with 20 in the nested list[[1,2,3],[4,5,6]]
li=[[1,2,3],[4,5,6]]
li[0][1]=20
print(li)

#Add a new sublist[7,8,9] to the existing nested list
nested_list=[[1,2,3],[4,5,6]]
nested_list.append([7,8,9])
print(nested_list)

#print the length of the nested list[[1,2],[3,4],[5,6]]
nested_list=[[1,2],[3,4],[5,6]]
print(len(nested_list))

#print each sublist in the nested list[[10,20],[30,40],[50,60]] using a loop
mat=[[10,20],[30,40],[50,60]]
for x in mat:
    print(x)

#print each element inside the nested list[1,2][3,4][5,6] using nested loop
mat=[[1,2],[3,4],[5,6]]
for x in mat:
    for y in x:
        print(y,end=" ")

#flatten the nested list[[1,2],[3,4],[5,6]] in to a single list
nested_list=[[1,2],[3,4],[5,6]]
flat=sum(nested_list,[])
print(flat)

#check if the number 4 exists in any sublist of[[1,2],[3,4],[5,6]].
nested_list=[[1,2],[3,4],[5,6]]
for x in nested_list:
    if 4 in x:
        print(f"4 exists in:",x)

#sum all the numbers in the nested list [[1,2],[3,4],[5,6]]
nested_list=[[1,2],[3,4],[5,6]]
flat=sum(nested_list,[])
print(sum(flat))
















        





