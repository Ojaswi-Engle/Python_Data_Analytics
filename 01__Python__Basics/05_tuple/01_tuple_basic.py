'''tuples are the datatype in python.
They are similar to list but the only difference between tuple and list is 
that we cannot change the elements of tuple once they are assigned ,
whereas we can change the elements of the list .

characterstics of tuple- ordered,indexed,immutable,dynamic,
heterogenous dataitems,nesting allowed , duplicates allowed
'''

#create tuple
t1=()
print(t1)
#create tuple with single element
t2=('hi',)
print(t2)
print(type(t2))
print((3),type((3)))
#homogenous tuple 
t3=(1,2,3,4,5)
print(t3)
#heterogenous tuple 
t4=(1,2.5,True,'hi',[1,2,3])
print(t4)
#nested tuple
t5=(1,2,3,4,(5,6))
print(t5)
#tuple function
t6=tuple('hello')
print(t6)

#accessing elements of tuple 1.indexing   2.slicing 
t=(1,2,3,4,5)
print(t)
print(t[0])
print(t[-1])
print(t[4])
#slicing
print(t[0:3])
print(t[::-1])
print(t[-4:-2])


# editing , adding elements is not possible in tuples 
# whereas whole tuple can be deleted by del keyword   


#operations on tuple 
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
print(t1*3)
print(4 in t1)

for i in t1:
    print(i,end=' ')
print()
#tuple functions - len,min,max,sorted,reverse sorted,sum,del,count,index
t=(1,2,3,4,5,6,7,1)
print(t)

#len
print(len(t))

#min
print(min(t))

#max
print(max(t))

#sum
print(sum(t))

#sorted
print(sorted(t))

#reverse
print(sorted(t,reverse=True))

#count
print(t.count(1))

#index
print(t.index(5))

'''Difference between Lists and Tuples
Syntax
Mutability
Speed
Memory
Built in functionality
Error prone
Usability'''

#tuple unpack
a,b,c =(1,2,3)
print(a)
print(b)
print(c)

#swapping directly
a,b=b,a
print(a)
print(b)

#*others
a,b,*others=(1,2,3,4,5)
print(a)
print(b)
print(others)

#zip function 
a=(1,2,3)
b=(5,6,7)
print(tuple(zip(a,b)))





