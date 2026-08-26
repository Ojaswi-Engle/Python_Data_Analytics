'''list - It is a datatype in python which is used to store multiple data items in 1.

array vs list 
1. static vs dynamic 
2.homogenous vs heterogenous 
3.fast vs slower speed of execution 
4.small space vs large  space

list - it stores memory address of actual data item (reference) not actual value 

characterstics 
1.ordered
2.indexing
3.mutable
4.heterogenous
5.dynamic
6.nesting allowed
7.duplicate allowed
8.can store any kind of object in python
'''

#create list 
#empty
print([])
#1d 
print([1,2,3,4])
#2d
print([1,2,3,[4,5]])
#3d 
print([1,2,3,[4,5,[6,7]],10])
#heterogenous 
print(['hello',1,5.6,True])
#list()
print(list('hello'))

#access list - 1.indexing    2.slicing
l=[1,2,3,4,5]
print(l[3]) #+ve indexing 
print(l[-4])#-ve 

l=[1,2,3,[4,5]]
print(l[3][0])
print(l[-1][-2])
l=[[1,2,[4,5],3],[4,5],[1,[2,3],4]]
print(l[0][2][0])
print(l[2][1][1])
print(l[1][0])

#slicing 
l=[1,2,3,4,5,6]
print(l[0:3])
print(l[-5:-1])
print(l[-2:-5:-1])
print(l[::2])
print(l[-5:3])

#add element in list 
l=[1,2,3,4,5,6]
#append
l.append(7)
print(l)
l.append([3,4])
print(l)

#extend
l.extend([9,8,10])
print(l)
l.extend('abc')
print(l)

#insert
l.insert(5,'oju')
print(l)

#editing items in list
#indexing 
l=[1,2,3,4,5,6]
l[0]='@'
print(l)
l[-2]=900
print(l)

#slicing
l[2:5]=['#']
print(l)

#delete 
#del
l=[1,2,3,4,5]
print(l)
del l
l=[1,2,3,4,5,6]
del l[2]
print(l)
del l[2:]
print(l)

#remove
l=[1,2,3,4,5,6,7,8,2]
l.remove(2)
print(l)

#pop
l.pop(4)
print(l)
l.pop()
print(l)

#clear
l.clear()
print(l)

#operations 
#arithmetic 
l1=[1,2,3,4]
l2=[5,6,7,8,[9,11]]
print(l1+l2)
print(l1*3)

#membership
print(4 in l1)
print(9 in l2)

#loops 
for i in l1:
    print(i,end=' ')
print()
for i in l2:
    print(i,end='  ')
print()


#functions 
l=[2,1,4,3,5]
print(l)

#len
print(len(l))

#min
print(min(l))

#max
print(max(l))

#sorted
print(sorted(l))

#reverse sorted 
print(sorted(l,reverse=True))


#count
print(l.count(3))

#index
print(l.index(3))

#reverse
l.reverse()
print(l)

#sort
l.sort()
print(l)

#copy
l2=l.copy()
print(id(l))
print(id(l2))  #different address because it is copy of first one 
