#Bubble - sort
list=[15,33,6,77,4,12,5,7,2]
n=len(list)
for i in range(n-1):
  for j in range(n-i-1):
    if list[j]>list[j+1]:
      list[j],list[j+1] = list[j+1],list[j]
print(list)



#Selection - sort
list=[67,5,35,6,2,3,8,16,9,1]
n=len(list)
for i in range(n-1):
  min_index=i
  for j in range(i+1,n):
    if list[j] < list[min_index]:
      min_index=j
  list[i],list[min_index] = list[min_index],list[i]
print(list)


#Insertion - sort
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist[i]
  for j in range(i-1, -1, -1):
     if mylist[j] > current_value:
       mylist[j+1] = mylist[j]
       insert_index = j
     else:
       break
  mylist[insert_index] = current_value
print(mylist)
