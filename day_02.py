#Bubble - sort
list=[15,33,6,77,4,12,5,7,2]
n=len(list)
for i in range(n-1):
  for j in range(n-i-1):
    if list[j]>list[j+1]:
      list[j],list[j+1] = list[j+1],list[j]
print(list)




