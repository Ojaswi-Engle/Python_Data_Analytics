#add 1 to 10 numbers in a list
#logic 1 loops
l=[]

for i in range(1,11):
    l.append(i)

print(l)

#logic 2

l2=[i for i in range(1,11) ]
print(l2)

#scalar multiplication to vector
#logic 1
v=[2,3,4]
s=-3
result=[]

for i in v:
    result.append(s*i)

print(result)

#logic 2
result=[i*s for i in v]
print(result)


#add squares 
#logic 1
n=int(input("enter a number:"))
result=[]
for i in range(1,n+1):
    result.append(i*i)
print(result)

#logic2
result=[i*i for i in range(1,n+1)]
print(result)

#print all numbers in the range (1,50) which are divisible by 5
#logic 1
l=1
h=50
result=[]
for i in range(l,h+1):
    if i % 5==0:
        result.append(i)
print(result)

#logic 2
result=[ i   for i in range(l,h+1) if i % 5==0]
print(result)

#select all the languages starts with p 
languages=['java','python', 'php','c','javascript']
p=[]

for l in languages:
    if l.startswith('p'):
        p.append(l)
print(p)

#logic 2
p=[    l   for l in languages   if l.startswith('p')]
print(p)

#add new list containg fruits from my_fruits which belongs to basket and startswith a. and
#logic 1

basket=['apple','guava','cherry','banana']
my_fruits=['apple','kiwi','grapes','banana'] 

result=[]

for fruit in my_fruits:
    if fruit in basket:
        if fruit.startswith('a'):
            result.append(fruit)
print(result)


#logic 2
result=[    fruit     for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
print(result)

# print a 3 X 3 matrix 
#logic 1
matrix=[]
for i in range(3):
    row=[]
    for j in range(1,4):
        row.append(i+j)
    matrix.append(row)
print(matrix)

#logic 
matrix=[[i+j  for j in range(1,4)]        for i in range(3)]
print(matrix)


#cartesian product 
l1=[1,2,3,4]
l2=[5,6,7,8]
#logic 1
result=[]
for i in l1:
    for j in l2:
        result.append(i*j)
    
print(result)

#logic 2
result=[  i*j           for i in l1   for j in l2]
print(result)


