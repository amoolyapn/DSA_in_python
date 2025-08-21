#printing  umbers in pairs
L=[1,2,3,4,5]
for i in range L:
  for j in rangr L:
print('({},{})'.format(i,j))


#converting intToStr
def intToStr(i):
  digits='01234'
  if i==0:
    return 0
  result=''
  while i>0:
    result=digits[i %10]+result
    i=i//10
  return result
print(intToStr(123))


#reversing a list
L=[1,2,3,4,5]
for i in range(0,len(L)//2):
  other=len(L)-i-1
  temp=L[i]
  L[i]=L[other]
  L[other]=temp
print(L)

#Dynamic array
#1
import sys
L=[]
sys.getsizeof(L)
L.append(128)
L.append("HI")
L
sys.getsizeof(L)

#2
L=[]
for i in range(50):
  print(i,sys.getsizeof(L))
  L.append(i)
