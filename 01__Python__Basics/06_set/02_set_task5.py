'''Q1: Write a program to find set of common elements in three lists using sets.
Input : ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

Output : [80, 20]'''
ar1=[1,5,10,20,40,80]
ar2=[6,7,20,80,100]
ar3=[3,4,15,20,30,70,80,120]

result=set()

for i in ar1:
    if i in ar2 and i in ar3:
        result.add(i)
print(result)

#logic 2

ar1=[1,5,10,20,40,80]
ar2=[6,7,20,80,100]
ar3=[3,4,15,20,30,70,80,120]

print(set(ar1) & set(ar2) & set(ar3))

'''Q2: Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.
Input:

Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
Output:

No of unique vowels-6'''
string='hands-on data science mentorship progrAm with live classes at affordable fee only on campusX'
vowel={'a','e','i','o','u','A','E','I','O','U'}
count=0 

for i in vowel:
    if i in string:
        count+=1

print('No of unique vowels-',count)

#logic 2
string='hands-on data science mentorship progrAm with live classes at affordable fee only on campusX'
vowel={'a','e','i','o','u','A','E','I','O','U'}

temp=vowel.intersection(string)
print('No of unique vowels-',len(temp))

'''Q3: Write a program to Check if a given string is binary string of or not.
A string is said to be binary if it's consists of only two unique characters.

Take string input from user.

Input: str = "01010101010"
Output: Yes

Input: str = "1222211"
Output: Yes

Input: str = "Campusx"
Output: No'''
#logic 1

str='0101001010101010'
l=[]

for ch in str:
    if ch not in l:
        l.append(ch)

if len(l)==2:
    print('yes')
else:
    print('no')

#logic 2
s=set(str)
if len(s)==2:
    print('yes')
else:
    print('no')


'''find union of n arrays.
Example 1:

Input:

[[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]
Output:

[1, 2, 3, 4, 5, 6, 7, 9]

'''
#logic 1
arr=[
    [1,2,2,4,3,6],
    [5,1,3,4],
    [9,5,7,1],
    [2,4,1,3]
]
l=[]

for i in arr:
    for j in i:
        l.append(j)

print(set(l))

#logic 2
s=set()
for i in range(len(arr)):
    s=s.union(arr[i])
print(s)

'''Q5: Intersection of two lists. Intersection of two list means we need to take all 
those elements which are common to both of the initial lists and 
store them into another list. Only use using list-comprehension.
Example 1:

Input:

lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
Output:

[9, 10, 4, 5]
Example 2:

Input:

lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]

Output:

[9, 11, 26, 28]
'''
#logic 1
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
result=set()
for i in set(list1):
    if i in set(list2):
        result.add(i)
print(list(result))

#logic 2
print(list(set(list1).intersection(list2)))

#logic 3
print([  i    for i in set(list1)  if i in list2 ])