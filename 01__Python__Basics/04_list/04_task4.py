'''Problem 1: Combine two lists index-wise(columns wise)
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

Given List:

list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
Output:

[['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]'''

#logic 1
list1=input().split()
list2=input().split()
result=[]

list1_=list1.copy()
list2_=list2.copy()

for i in range(min(len(list1_),len(list2_))):
    result.append([list1_[i],list2_[i]])
    list1.remove(list1_[i])
    list2.remove(list2_[i])

if list1!=[]:
    result.extend(list1)
elif list2!=[]:
    result.extend(list2)
print(result)

#logic 2
list1=input().split()
list2=input().split()
result=[]

for i in range(min(len(list1),len(list2))):
    result.append([list1[i],list2[i]])

temp=min(len(list1),len(list2))

if len(list1)>len(list2):
    result+=list1[temp:]
elif len(list2)>len(list1):
    result+=list2[temp:]
print(result)

#logic 3

result=[  [i,j]     for i,j in zip(list1,list2) ]

temp=min(len(list1),len(list2))

if len(list1)>len(list2):
    result+=list1[temp:]
elif len(list2)>len(list1):
    result+=list2[temp:]
print(result)

'''Problem 2: Add new item to list after a specified item
Write a program to add item 7000 after 6000 in the following Python List

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]'''

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

for i in list1:
    if type(i)==list:
        for j in i:
            if type(j)==list:
                pos=j.index(6000)
                j.insert(pos+1,7000)
print(list1)

#logic 2
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
inner=list1[2][2]
pos=inner.index(6000)
inner.insert(pos+1,7000)
print(list1)

'''Problem 3: Update no of items available
Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

i.e -

candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
Write a program to show no. of items of each candy type.

Output:

Jelly Belly-10
Kit Kat-20
Double Bubble-34
Milky Way-74
Three Musketeers-32
'''

candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]

#logic 1
for i in range(len(candy_list)):
    print(candy_list[i]+'-',no_of_items[i],sep='')

#logic 2
for x,y in zip(candy_list,no_of_items):
    print(x+'-',y,sep='')

'''Problem 4: Running Sum on list
Write a program to print a list after performing running sum on it.

i.e:

Input:

list1 = [1,2,3,4,5,6]
Output:

[1,3,6,10,15,21]'''

list1 = [1,2,3,4,5,6]
sum_=0
result=[]

for i in list1:
    sum_+=i
    result.append(sum_)

print(result)

'''Problem 5: You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.
i.e. Say given list is [2,4,6,10,1] resultant list will be [22,20,10,23].

For 1st element 2 ->> these are greater (4+6+10) values and 2 itself so on adding becomes 22.

For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20

like wise for all other elememts.

[2,4,6,10,1]-->[22,20,16,10,23]

'''

l=list(map(int,input().split()))
result=[]

for i in l:
    sum_=0
    for j in l:
        if j>=i:
            sum_+=j
    result.append(sum_)
print(result)

'''Problem 6: Find list of common unique items from two list. and show in increasing order
Input

num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
Output:

[34, 67, 89]

'''

num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
result=[]

for i in num1:
    if i in  num2 and i not in result:
        result.append(i)

print(sorted(result))

'''Problem 7: Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
Input:

['1ac21', '23fg', '456', '098d','1','kls']
Output:

['456', '23fg', '1ac21', '1', 'kls', '098d']
'''
#logic 1
l=['1ac21', '23fg', '456', '098d','1','kls']
p=[]

for s in l:
    prod=1
    present=False
    for ch in s:
        if ch.isdigit():
            prod*=int(ch)
            present=True
    if present:
        p.append(prod)
    else:
        p.append(1)

for k in range(len(p)-1):
    for m in range(len(p)-1-k):
        if p[m]<p[m+1]:
            p[m],p[m+1]=p[m+1],p[m]
            l[m],l[m+1]=l[m+1],l[m]
print(l)

#logic 2
l=['1ac21', '23fg', '456', '098d','1','kls']
p=[]

for s in l:
    prod=1
    present=False
    for ch in s:
        if ch.isdigit():
            prod*=int(ch)
            present=True
    if present:
        p.append(prod)

    else:
        p.append(1)

for k in range(len(p)-1):
    max=k
    for m in range(k+1,len(p)):
        if p[m]>p[max]:
            max=m
    p[k],p[max]=p[max],p[k]
    l[k],l[max]=l[max],l[k]

'''Problem 8: Split String of list on K character.

Example :

Input:

['CampusX is a channel', 'for data-science', 'aspirants.']
Output:

['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']
'''
'''Problem 8: Split String of list on K character.

Example :

Input:

['CampusX is a channel', 'for data-science', 'aspirants.']
Output:

['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']
'''
#logic 1

l=['CampusX is a channel', 'for data-science', 'aspirants.']
result=[]

for string in l:
    word=''
    for ch in string:
        if ch!=' ':
            word+=ch
        else:
            if word!='':
                result.append(word)
                word=''
    if word!='':
        result.append(word)

print(result)

#logic 2
l=['CampusX is a channel', 'for data-science', 'aspirants.']
s=' '.join(l)
l=s.split()
print(l)  

'''Problem 9: Convert Character Matrix to single String using string comprehension.
Example 1:

Input:

[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
Output:

campux is best channel

'''
#logic 1
l=[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
counter=len(l)
s=''

for i in l:
    for j in i:
        s+=j
    counter-=1
    if counter!=0:
        s+=' '
print(s)

#logic 2
l=[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
result=[  ''.join(i)      for i in l]

print(' '.join(result))

'''Problem 10: Add Space between Potential Words.
Example:

Input:

['campusxIs', 'bestFor', 'dataScientist']
Output:

['campusx Is', 'best For', 'data Scientist']

'''
#logic 1

l=input().split()
result=[]

for s in l:
    word=''
    index=0
    for ch in s:
        if index==0 and ch.isupper():
            word+=ch
        elif ch.isupper():
            word=word+' '+ch
        else:
            word+=ch
        index+=1
    result.append(word)
print(result)

#logic 2
l=input().split()
for i in range(len(l)):
    word=''
    index=0
    for ch in l[i]:
        if index==0 and ch.isupper():
            word+=ch
        elif ch.isupper():
            word=word+' '+ch
        else:
            word+=ch
        index+=1
    l[i]=word
print(l)
#logic 3
l=input().split()
result=[]
for s in  l:
    l_=list(s)
    shift=0
    for i in range(len(s)):
        if i!=0 and s[i].isupper():
            l_.insert(i+shift,' ')
            shift+=1
    result.append(''.join(l_))
print(result)

#logic 4
l=input().split()
result=[]
for s in  l:
    l_=list(s)
    shift=0
    for i in range(len(s)):
        if i!=0 and l_[i+shift].isupper():
            l_.insert(i+shift,' ')
            shift+=1
    result.append(''.join(l_))
print(result)


'''Problem 11:  Write a program that can perform union operation on 2 lists
Example:

Input:

[1,2,3,4,5,1]
[2,3,5,7,8]
Output:

[1,2,3,4,5,7,8]'''

list1=list(map (int,input().split()))
list2=list(map (int,input().split()))
result=[]
total=list1+list2

for i in total:
    if i not in result:
        result.append(i)

print(sorted(result))

'''Write a program that can find the max number of each row of a matrix
Example:

Input:

[[1,2,3],[4,5,6],[7,8,9]]
Output:

[3,6,9]

'''
#logic 1
matrix=[]
result=[]
n=int(input("enter number of rows:"))
for i in range(n):
    row=list( map(int,input("enter values:").split()))
    matrix.append(row)

for i in matrix:
    max_value=i[0]
    for j in range(1,len(i)):
        if i[j]>max_value:
            max_value=i[j]
    result.append(max_value)

print(result)

#logic 2
matrix=[]

n=int(input("enter number of rows:"))
for i in range(n):
    row=list( map(int,input("enter values of : ").split()))
    matrix.append(row)


result=[ max(i)     for i in matrix]
print(result)

'''Problem 13: Write a list comprehension to print the following matrix
[[0, 1, 2], [3, 4, 5], [6, 7, 8]]


[ ]
'''

#logic 1
matrix=[]
a=0
for i in range(3):
    row=[]
    for j in range(3):
        row .append(a)
        a+=1
    matrix.append(row)
print(matrix)

#logic 2
result=[ [ i*3+j       for j in range(3)]    for i in range(3)]
print(result)

'''
Problem 14: Write a list comprehension that can transpose a given matrix
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
'''
#logic 1
n=int(input("enter number of rows:"))
matrix=[]
for i in range(n):
    row=list(map(int,input("enter values:").split()))
    matrix.append(row)

transpose=[]

for i in range(len(matrix)):
    row=[]
    for j in range(len(matrix[i])):
        row.append(matrix[j][i])
    transpose.append(row)
print(transpose)

#logic 2
n=int(input("enter number of rows:"))
matrix=[]
for i in range(n):
    row=list(map(int,input("enter values:").split()))
    matrix.append(row)

transpose=[ [  matrix[j][i]  for j in range(len(matrix[i]))] for i in range(len(matrix))]
print(transpose)

'''Problem 15: Write a list comprehension that can flatten a nested list
Input
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

l=[]
n=int(input("enter number of  rows:"))
for i in range(n):
    row=list(map(int,input("enter values:").split()))
    l.append(row)
result=[]
for j in l:
    for k in j:
        result.append(k)
print(result)

#logic 2
result=[   j        for i in l    for j in i]
print(result)