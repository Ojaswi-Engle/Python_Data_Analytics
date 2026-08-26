#create 2 list where
#1st list will contail all the odd numbers from the original list and 2nd will contain all the evens

l=[1,2,3,4,5,6]
l_odd=[]
l_even=[]

for i in l:
    if i % 2!=0:
        l_odd.append(i)
    else:
        l_even.append(i)
        
print(l_odd)
print(l_even)

#logic 2
l=[1,2,3,4,5,6]
l_odd=[i for i in l if i%2!=0]
l_even=[i for i in l if i%2==0]

print(l_odd)
print(l_even)

#how to take list as input from user
#logic 1 
n=int(input("enter number:"))
l=[]
for i in range(n):
    l.append(int(input()))
print(l)

#logic 2 
                          
l=list( map(int,input("enter numbers:").split()))
print(l)

#logic 3
l=[    int(i)       for i in input("enter numbers").split()]
print(l)

#wap to merge two list without using + operator
#logic 1
l1=[1,2,3,4]
l2=[5,6,7,8]
l=[]

for i in l1:
    l.append(i)

for i in l2:
    l.append(i)
print(l)

#logic 2

l1.extend(l2)
print(l1)

#logic 3
l1=[1,2,3,4]
l2=[5,6,7,8]
l=l1.copy()
l.extend(l2)
print(l)

#logic 4
l1=[1,2,3,4]
l2=[5,6,7,8]
l=[i for i in l1]
for i in l2:
    l.append(i)
    
print(l)

#logic 5 
l=l1.copy()
for i in l2:
    l.insert(len(l),i)
print(l)


#wap to replace an item with different item if found in the list 
l=[1,2,3,4,5,3]
r=3
replace_by=300

#logic 1
if r in l:
    for i in range(len(l)):
        if l[i]==r:
            l[i]=replace_by
    print(l)
else:
    print("replacement not possible")

#logic 2
l=[1,2,3,4,5,3]
r=3
replace_by=300

#logic 3
if r in l:
    result=[    replace_by      if i == r   else  i      for i in l]
    print(result)
else:
    print("replacement not possible")

#convert 2d list to 1d
two_d=[1,2,3,4,[5,6]]
one_d=[]

for i in two_d:
    if type(i)==list:
        for j in i:
            one_d.append(j)
    else:
        one_d.append(i)
print(one_d)

#remove duplicate from list
l=[1,2,1,2,3,4,5,3,4]
result=[]

for i in l:
    if i not in result:
        result.append(i)

print(result)

#wap to check if the list is in ascending order or not 
#logic 1
l=list(map(int,input("enter numbers:").split()))

if sorted(l)==l:
    print("ascending ")
else:
    print(" not ascending ")

#logic 2 
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        print(" not ascending ")
        break
else:
    print("ascending ")
