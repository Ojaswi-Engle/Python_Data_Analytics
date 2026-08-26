#strings are the sequence of characters(unicode characters - 16 bit based system)

#create string 
s='Hi,I am Ojaswi'
print(s)

s="Hi,I am Ojaswi"
print(s)

s='''Hi,I am Ojaswi'''
print(s)

s=str('hello World')
print(s)

#accessing strings by indexing 
#positive indexing
print(s[0])
print(s[4])
#negative indexing
print(s[-3])

#slicing
print(s[1:5])
print(s[7:10])

print(s[:5])
print(s[2:])
print(s[:])

print(s[2:10:2])
print(s[2:10:3])
print(s[-10:-2])

#negative step count
print(s[10:1:-1])
print(s[-1:-10:-1])
print(s[-11:])
print(s[:-3])
print(s[:2:-1])
print(s[2:0])#empty string 
print(s[::-1])
print(s[0:100])# extra characters empty 

#editing s[0]='s' not possible strings are immutable 
#deleltion of string 
s2='star fish'
del s2
#print(s2)

#operations on strings 
#arithmetic op
s3='hello'+" ojaswi"
print(s3)

print(s3*4)

#relational op

print('hello' < 'world')#compare char by char by ascii values
print('hello' > 'world')
print('hhab'<'hhAb')
print('delhi'=='delhi')

#logical op
print('abc' and 'xyz')
print('abc' and '')
print('' and 'xyz')

print('abc' or 'xyz')
print('abc' or '')
print('' or 'xyz')

print(not '')
print(not 'abc')

#loops 
for i in 'ojaswi':
    print(i,end=' ')

for i in 'ojaswi':
    print("*",end='-')

#membership
print('o' in 'ojaswi')
print('#' in 'khargone')
print('oj' in 'ojaswi')
