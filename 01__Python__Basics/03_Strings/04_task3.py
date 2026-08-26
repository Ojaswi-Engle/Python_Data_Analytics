'''Problem 1 - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1'''

n=int(input("enter a number:"))

for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(j,end='')
    print()

'''Problem 2: Print the following pattern.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*'''

n=int(input("enter a number:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()
for i in range(1,n):
    for j in range(n-i,0,-1):
        print('*',end='')
    print()

'''
Problem 3:Write a program to pring the following pattern
    *
  * * *
* * * * *

'''
'''Problem 2: Print the following pattern.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*'''

n=int(input("enter a number:"))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end='')
    for j in range(1,2*i):
        print('*',end='')
    print()



'''
Problem 4:Write a program to print the following pattern
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''

n=int(input("enter a number:"))

for i in range(1,n+1):
    a=i
    for j in range(1,i+1):
        print(a,end='')
        a-=1
    print()

'''
Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user
'''

n=int(input("enter number of terms:"))
x=int(input("enter a number:"))

sum_=0
product=x

for i in range(1,n):
    product*=x
    term=product/(i+1)
    sum_+=term
sum_+=1
print("sum:",sum_)

#problem6  sum of natural logarithmic approximate series

n=int(input("enter number of terms:"))
x=int(input("enter a number:"))

sum_=0
term=((x-1)/x)
value=((x-1)/x)
for i in range(1,n):
    term*=value
    
    sum_+=term
sum_=value + (0.5 * sum_)
print("sum:",sum_)


'''
Problem 7 - Find the sum of the series upto n terms.
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.

Example 1:
Input:
5
Output:
2+22+222+2222+22222
Sum of above series is: 24690
'''
n=int(input("enter number of terms:"))

sum_=0
s=''
series=''
for i in range(n):
    s+='2'
    if i==0:
        series=s
    else:
        series+='+'+s

    sum_+=int(s)
print(series)
print('Sum of above series is:',sum_)

'''Problem 8: Write a program to print all the unique combinations of 1,2,3 and 4
Output:

1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
.
.
and so on
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for l in range(1,5):
                if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                    print(i,j,k,l,sep=' ')



'''
Problem 9: Write a program that will take a decimal number as input and prints out the binary equivalent of the number

'''

deci=int(input("enter decimal number:"))
bin=0
a=1

while deci!=0:
    r=deci%2
    bin+=r*a
    a*=10
    deci//=2
print(bin)


'''
problem 10: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers
'''
#logic 1
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
a=n1
b=n2

'''for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        hcf=i

lowest=max(n1,n2)

while True:
    if lowest % n1==0 and lowest % n2==0:
        lcm=lowest
        break
    lowest+=1
print("hcf",hcf)
print('lcm',lcm)'''
#logic 2
'''l1=[]
l2=[]
common=[]
i=2
j=2

while n1!=1:
    if n1 % i==0:
        n1=n1//i
        l1.append(i)
    else:
        i+=1
while n2!=1:
    if n2 % j==0:
        n2=n2//j
        l2.append(j)
    else:
        j+=1
l1_=l1.copy()
for k in l1:
    if k in l2:
        common.append(k)
        l1_.remove(k)
        l2.remove(k)

prod=1
for l in common:
    prod*=l

lcm=prod
for m in l1_:
    lcm*=m

for n in l2:
    lcm*=n
print("hcf",prod)
print('lcm',lcm)'''

#logic 3 euclidean algo
while n2!=0:
    r=n1%n2
    n1=n2
    n2=r
hcf=n1
lcm=a*b//hcf
print("hcf",hcf)
print('lcm',lcm)


'''
Problem 11: Create Short Form from initial character
Given a string create short form ofthe string from Initial character. Short form should be capitalised.

Example:

Input:

Data science mentorship program
Output:

DSMP
'''

s=input("enter a string:")
shortform=''

s=s.title()
l=s.split()

for word in l:
    shortform+=word[0]

print("shortform : ",shortform)

'''Problem 12: Append second string in the middle of first string
Input:

campusx
data
Output:

camdatapusx'''
#logic1
first=input("enter first string:")
second=input("enter second string:")
result=''
'''result=first[0:len(first)//2]+second+first[len(first)//2:]
print(result)'''

#logic 2

for i in range(len(first)):
    result+=first[i]

    if i==(len(first)//2)-1:
        result+=second
print(result)


'''Problem 13:Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
Given:

str1 = PyNaTive

Expected Output:

yaivePNT'''

s=input("enter a string:")
lower=''
upper='' 
result=''

for ch in s:
    if ch.islower():
        lower+=ch
    if ch.isupper():
        upper+=ch
result=lower+upper
print(result)


'''Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
Input:

hel123O4every093

Output:

Sum: 22
Avg: 2.75

'''
s=input("enter a string:")
total=0
average=0
count=0

for ch in s:
    
    if ch.isdigit():
        total+=int(ch)
        count+=1

if count==0:
    print('no digits present')
else:
    average=total/count
    print("sum = ",total)
    print("average = ",average)

'''Problem 15: Removal of all characters from a string except integers
Given:

str1 = 'I am 25 years and 10 months old'
Expected Output:

2510'''

s=input("enter  a string:")
result=''

for ch in s:
    if ch.isdigit():
        result+=ch
print(result)

'''problem 16 is Symmetrical.
Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.

Example 1:

Input

khokho
Output

The entered string is symmetrical'''

#logic 1
s=input("enter a string:")

'''if len(s) % 2==0:
    for i in range(len(s)//2):
        if s[i] != s[i+len(s)//2]:
            print('the entered string is unsymmetrical')
            break

    else:
        print('the entered string is symmetrical')
else:
    print('entered string is unsymmetrical')'''
#logic 2


if len(s) % 2==0:
    s1=s[0:len(s)//2]
    s2=s[len(s)//2:]
    if s1==s2:
            print('the entered string is symmetrical')
            

    else:
        print('the entered string is unsymmetrical')
else:
    print('entered string is unsymmetrical')

'''Problem 17: Reverse words in a given String
Statement: We are given a string and we need to reverse words of a given string.'''

s=input("enter  a string:")

l=s.split()

for i in range(len(l)//2):
    temp=l[i]
    l[i]=l[len(l)-1-i]
    l[len(l)-1-i]=temp

s=' '.join(l)
print(s)


'''Problem 18: Find uncommon words from two Strings.
Statement: Given two sentences as strings A and B.
 The task is to return a list of all uncommon words. A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. 
 Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters'''

A=input("enter first string:")
B=input("enter second string:")
uncommon=[]

a=A.split()
b=B.split()

all_words=a+b

for word in all_words:
    if all_words.count(word)==1:
        uncommon.append(word)

print(uncommon)

'''Problem 19: Word location in String.
Statement: Find a location of a word in a given sentence.

Example 1:

Input:

Sentence: We can learn data science through campusx mentorship program.

word: campusx
Output:

Location of the word is 7.
Note- Don't use index/find functions


'''

s=input("Sentence:")
word=input("word:")
l=s.split()

if word in l:
    
    location=0
    
    for w in l:
        location+=1
        if w==word:
            print("Location of the word is ",location,'.',sep='')
            break
else:
    print("word is not present")

'''Problem 20: Write a program that can remove all the duplicate characters from a string. 
User will provide the input.'''

s=input("enter a string:")
result='' 

for ch in s:
    if ch not in result:
        result+=ch

print(result)
