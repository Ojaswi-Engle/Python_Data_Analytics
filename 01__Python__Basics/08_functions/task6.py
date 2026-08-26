'''Problem-1: Write a Python function that takes a list and returns a new list with unique elements of the first list.
Exercise 1:

Input:

[1,2,3,3,3,3,4,5]
Output:

[1, 2, 3, 4, 5]

'''
#logic 1
def remove_1(list):
    res=sorted(set(list))
    return res
l=list(map(int,input().split()))

ans=remove_1(l)
print(ans)

#logic 2
def remove_2(list):
    res=[]
    for i in list:
        if i not in res:
            res.append(i)

    return res


l=list(map(int,input().split()))
ans=remove_2(l)
print(ans)

#logic 3
def remove_3(remove,list,res):
    for i in list:
        if not remove(i):
            res.append(i)
    return res

l=list(map(int,input().split()))
res=[]
ans=remove_3(lambda x: x in res,l,res)
print(ans)

'''Problem-2: Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.
Example 1:

Input:

green-red-yellow-black-white
Output:

black-green-red-white-yellow

'''
def sort(str):
    l=str.split('-')
    l=sorted(l)
    str='-'.join(l)
    return str
s=input()
ans=sort(s)
print(ans)

'''Problem 3: Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
Expected Output :
No. of Upper case characters :  9
No. of Lower case Characters :  47

'''
#logic 1
def count_letter(string):
    upper_count=0
    lower_count=0
    for ch in string:
        if ch !=' ':
            if ch.isupper():
                upper_count+=1
            else:
                lower_count+=1
    print('No. of Upper case characters :',upper_count)
    print('No. of lower case characters :',lower_count)
s=input()
count_letter(s)

#logic 2
def count_letter2(string):
    d={'upper':0,'lower':0}
    for ch in string:
        if ch!=' ':
            if ch.isupper():
                d['upper']+=1
            else:
                d['lower']+=1
    return d
s=input()
ans=count_letter2(s)
print('No. of Upper case characters :',ans['upper'])
print('No. of lower case characters :',ans['lower'])

'''Problem 4: Write a Python program to print the even numbers from a given list.'''
#logic1
def select1 (list):
    res=[]
    for i in list:
        if i%2==0:
            res.append(i)
    return res
l=list(map(int,input().split()))
ans=select1(l)
print(ans)

#logic 2
l=list(map(int,input().split()))
ans=list(filter(lambda x:x%2==0,l))
print(ans)

#logic 3
def select3(even,lst):
    res=[]
    for i in lst:
        if even(i):
            res.append(i)
    return res

l=list(map(int,input().split()))
ans=select3(lambda x:x%2==0,l)
print(ans)

'''Problem 5: Write a Python function to check whether a number is perfect or not.
A Perfect number is a number that is half the sum of all of its positive divisors (including itself).

Example :

The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 

The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

'''
def divisors(n):
    d=[]
    for i in range(1,n+1):
        if n%i==0:
            d.append(i)
    return d
def add(l):
    sum_=0
    for i in l:
        sum_+=i
    return sum_
def check(d,x,n):
    divisor=d(n)
    s=x(divisor)
    if n==s//2:
        return True
    else:
        return False
n=int(input())
if(check(divisors,add,n)):
    print('perfect')
else:
    print('not perfect')

'''Problem-6: Write a Python function to concatenate any no of dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

'''
def concatenate(*args):
    res={}
    for i in args:
        res.update(i)
    return res
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
ans=concatenate(dic1,dic2,dic3)
print(ans)

'''Problem-7 Write a python function that accepts a string as input and returns the word with most occurence.

Input:
hello how are you i am fine thank you
Output
you -> 2

'''
def occurence (s):
    l1=s.split()
    st=set(l1)
    l2=list(st)
    c=[]
    for word in l2:
        c.append(l1.count(word))
    value=max(c)
    pos=c.index(value)
    return (l2[pos],value)

string=input()
ans=occurence(string)
print(ans[0],'->',ans[1])

#logic 2
def occurence2(s):
    l=s.split()
    st=set(l)
    d={}
    for word in st:
        d[word]=l.count(word)
    val=max(d.items(),key=lambda x:x[1])
    return val

string=input()
ans=occurence2(string)
print(ans[0],'->',ans[1])

'''Problem-8 Write a python function that receives a list of integers and prints out a histogram of bin size 10

Input:
[13,42,15,37,22,39,41,50]
Output:
{11-20:2,21-30:1,31-40:2,41-50:3}

'''
#logic 1
def histogram(l,bs):
    d={}
    start=((min(l)-1)//bs)*bs+1
    end=((max(l)-1)//bs)*bs+1
    higher=start+bs-1

    while start<=end:
        lower=start
        d[(lower,higher)]=0
        start=higher+1
        higher=higher+bs

    for val in l:
        for ((i,j),k) in d.items():
            if val>=i and val<=j:
                d[(i,j)]+=1

    res= dict(map(lambda x:(str(x[0][0])+'-'+str(x[0][1]),x[1]), d.items()))
    return res

lst=list(map(int,input().split()))
bin_size=10
ans=histogram(lst,bin_size)
print(ans)

#logic 2
def histogram(l,bs):
    d={}
    for i in l:
        lower=((i-1)//bs)*bs+1
        higher=lower+bs-1
        if (lower,higher) not in d:
            d[(lower,higher)]=0
        d[(lower,higher)]+=1
    res=dict(map(lambda x:(str(x[0][0])+'-'+str(x[0][1]),x[1]),d.items()))
    return res

lst=list(map(int,input().split()))
bin_size=10
ans=histogram(lst,bin_size)
print(ans)

#logic 3
def histogram(l,bs):
    start=((min(l)-1)//bs)*bs+1
    end=((max(l)-1)//bs)*bs+1
    higher=start+bs-1
    d={}

    while start<=end:
        lower=start
        d[(lower,higher)]=0

        start=higher+1
        higher=higher+bs
    for i in l:
        lower=((i-1)//bs)*bs+1
        higher=lower+bs-1

        d[(lower,higher)]+=1
    res=dict(map(lambda x:(str(x[0][0])+'-'+str(x[0][1]),x[1]),d.items()))
    return res

lst=list(map(int,input().split()))
bin_size=10
ans=histogram(lst,bin_size)
print(ans)

'''problem 9:Problem-9 Write a python function that accepts a list of 2D co-ordinates and a query point, and then finds the the co-ordinate which is closest in terms of distance from the query point.

List of Coordinates
[(1,1),(2,2),(3,3),(4,4)]
Query Point
(0,0)
Output
Nearest to (0,0) is (1,1)
'''
#logic 1
def distance(c,q):
    res=((c[0]-q[0])**2+(c[1]-q[1])**2)**0.5
    res=int(res)
    return res
def calculate(d,l,q):
    dist=[]
    for i in l:
        dist.append(d(i,q))
    val=max(dist)
    pos=dist.index(val)
    return l[pos]


lst=[(1,1),(2,2),(3,3),(4,4)]
query=(0,0)
ans=calculate(distance,lst,query)
print(ans)

#logic 2
def distance(c,q):
    res=((c[0]-q[0])**2+(c[1]-q[1])**2)**0.5
    res=int(res)
    return res

def calculate(d,l,q):
    dist={}
    for i in l:
        dist[i]=d(i,q)
    val=max(dist,key=lambda x:dist[x])
    return val


lst=[(1,1),(2,2),(3,3),(4,4)]
query=(0,0)
ans=calculate(distance,lst,query)
print(ans)

#logic 1
def vocablury(l):
    s=' '.join(l)
    l=s.split()
    res=[]
    for i in l:
        if i not in res:
            res.append(i)
    return res
def bagofwords(v,l):
    vocab=v(l)
    res=[]
    for s in l:
        l_=s.split()
        temp=[]
        for word in vocab:
            temp.append(l_.count(word))
        res.append(temp)
        return res


n=int(input())
lst=[ input() for i in range(n)]
ans=bagofwords(vocablury,lst)
print(ans)
#logic 2
def vocablury(l):
    s=' '.join(l)
    l=s.split()
    res=[]
    for i in l:
        if i not in res:
            res.append(i)
    return res
def bagofwords(v,l):
    vocab=v(l)
    res=[]
    for s in l:
        l_=s.split()
        d={}
        for word in vocab:
            d[word]=l_.count(word)
        res.append(d)
    return res


n=int(input())
lst=[ input()  for i in range(n)]
ans=bagofwords(vocablury,lst)
print(ans) 


'''Problem 11: Write a Python program to add three given lists using Python map and lambda.
'''

#logic 1

def add(l1,l2,l3):
    res=[]
    for i in range(len(l1)):
        res.append(l1[i]+l2[i]+l3[i])
    return res

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
ans=add(l1,l2,l3)
print(ans)

#logic 2
def add(l1,l2,l3):
    res=[]
    for i,j,k in zip(l1,l2,l3):
        res.append(i+j+k)
    return res
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
ans=add(l1,l2,l3)
print(ans)

#logic 3
def add(l1,l2,l3):
    res=list(map(lambda x,y,z:x+y+z    ,l1,l2,l3))
    return res

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
ans=add(l1,l2,l3)
print(ans)

'''Problem-12:Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
Input:

list1 = [1,2,3,4,5,6]
Output:

[1,2,9,64,625,-]

'''
def power(b,p):
    ans=1
    for i in range(p):
        ans*=b
    return ans
def calculate(pow,l):
    res=[]
    for i in range(len(l)):
        res.append(pow(l[i],i))
    return res
l=list(map(int,input().split()))
ans=calculate(power,l)
print(ans)
#logic 2
def power(b,p):
    ans=1
    for i in range(p):
        ans*=b
    return ans
def calculate(pow,b):
    index=[]
    for i in range(len(b)):
        index.append(i)

    res=list(map(lambda x,y:pow(x,y),b,index))
    return res
l=list(map(int,input().split()))
ans=calculate(power,l)
print(ans)

#logic 3
def power(p,b):
    ans=1
    for i in range(p):
        ans*=b
    return ans
def calculate(pow,b):
    res=list(map(lambda x:pow(x[0],x[1]),enumerate(b)))
    return res
l=list(map(int,input().split()))
ans=calculate(power,l)
print(ans)


'''Problem-13 Using filter() and list() functions and .lower() method filter all the vowels in a given string.

'''
def filter_vowel(s,vowel):
    s=s.lower()
    res=list(filter(  lambda x: x in vowel ,s ))
    return res

string=input()
vowel={'a','e','i','o','u'}
ans=filter_vowel(string,vowel)
print(ans)

'''Problem-14: Use reduce to convert a 2D list to 1D'''
import functools
def convert(l):
    res=functools.reduce(lambda x,y:x+y,l)
    return res

n=int(input())
list=[list(map(int,input().split()))  for i in range(n)]
ans=convert(list)
print(ans)

''''''
def employee_filter(d):
    res=  list(map(  lambda x:x['fname']+' '+ x['lname'] , list(filter(lambda d:d['grade']=='highly-skilled',employees))))

    return res


employees= [
    {
        'fname':'Nitish',
        'lname':'Singh',
        'age' : 33,
        'grade':'skilled'
    },
    {
        'fname':'Ankit',
        'lname':'Verma',
        'age' : 34,
        'grade':'semi-skilled'
    },
    {
        'fname':'Neha',
        'lname':'Singh',
        'age' : 35,
        'grade':'highly-skilled'
    },
    {
        'fname':'Anurag',
        'lname':'Kumar',
        'age' : 30,
        'grade':'skilled'
    },
    {
        'fname':'Abhinav',
        'lname':'Sharma',
        'age' : 37,
        'grade':'highly-skilled'
    }
]
ans=employee_filter(employees)
print(ans)