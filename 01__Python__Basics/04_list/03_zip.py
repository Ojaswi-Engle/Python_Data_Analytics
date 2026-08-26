#wap to add  items of two list indexed wise 
#logic 1
l1=[1,2,3,4]
l2=[-1,-2,-3,-4]
result=[]

for i in range(len(l1)):
    result.append(l1[i]+l2[i])
print(result)

#logic 2
result=[]
for x,y in zip(l1,l2):
    result.append(x+y)
print(result)

#logic 3
result=[x+y  for x,y in zip(l1,l2)]
print(result)