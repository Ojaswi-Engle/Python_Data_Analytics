#sets 
'''Sets
A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

However, a set itself is mutable. We can add or remove items from it.

Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

Characterstics:

Unordered
Mutable
No Duplicates
Can't contain mutable data types'''

#create 

s1=set()
print(s1)

#1D or 2D
s2={1,2,3,4,5}
print(s2)

#s3={1,2,3,4,{3,4}}  not allowed
#print(s3)

#homo hetero 
s4={1,2,3,6,4,5}
s5={True,'hi',1,4.5,None}
print(s4)
print(s5)

#set function 
print(set({1,2,3,4,6}))

#unordered 
s6={1,2,3,4}
s7={4,3,2,1}
print(s6==s7)

#no duplicates
print({1,2,3,4,5,4,3,2})

# no accessing either by indexing or by slicing 
# no editing 

#adding 
s8={1,2,3,4,'hi'}
s8.add('hello')
print(s8)

#update 
s8.update((('delhi',1,2,3.5)))#any iterable 
print(s8)



#delete

#del s8
#print(s8)

#remove
s9={1,2,3.5,'hii','hello'}
s9.remove(3.5)
print(s9)

#discard
s9.discard(10)

#pop
x=s9.pop()
print(x)

#clear
s9.clear()
print(s9)

#set operations 
set1={1,2,3,3,4,5}
set2={'hi',4,5,6,7}

print(set1 | set2)#union 
print(set1 & set2)#intersection
print(set1 - set2)#difference
print(set1 ^ set2)#symmetric difference

#membership
print('hi' in set2)

#iteration 
for i in set1:
    print(i,end=' ')
print()
#set functions
#len
print(len(set1))

#min
print(min(set1))

#max
print(max(set1))

#sorted
print(sorted(set1))

#reverse sorted
print(sorted(set1,reverse=True))

#sum
print(sum(set1))

set1={1,2,3,4}
set2={'hi',4,5,6,7}
#intersection_update/intersection  
print(set1.intersection(set2))
set1.intersection_update(set2)
print(set1)

#difference_update/difference
set1={1,2,3,4}
set2={'hi',4,5,6,7}
print(set1.difference(set2))
set1.difference_update(set2)
print(set1)

#symmetric_difference_update/symmetric_difference 
set1={1,2,3,4}
set2={'hi',4,5,6,7}
print(set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print(set1)

#update/union 
set1={1,2,3,4}
set2={'hi',4,5,6,7}
print(set1.union(set2))
set1.update(set2)
print(set1)

#issubset/issuperset/isdisjoint
set1={3,4}
set2={'hi',3,4,5,6,7}

print(set1.issubset(set2))
print(set2.issuperset(set1))

print(set1.isdisjoint(set2))


#frozenset
#Frozen set is just an immutable version of a Python set object
#create 
print(frozenset((1,2,3,4,6,5,'hiiii')))
#1D or 2D
s_=frozenset('hello')
s={1,2,3,4,5,s_}
print(s)

#del 
del s_

#frozenset operations - |,&,-,^
s1=frozenset({1,2,3,4,5})
s2=frozenset([1,2,8,9,90])

print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s1^s2)

#len/ min /max /sorted /reversesorted/sum as it ease of set 

#union/intersection/difference/symmetric_difference

print(s1.union(s2)) 
print(s1.intersection(s2)) 
print(s1.difference(s2)) 
print(s1.symmetric_difference(s2)) 







