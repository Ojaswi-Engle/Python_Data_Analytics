'functions '

#check if number is even or odd
def is_even(n):
    ''' this function returns if given number is even or odd
        input- any valid integer
        output-even/odd
    '''
    if n%2==0:
        return 'even'
    else:
        return 'odd'

n=int(input("enter a number:"))
print(is_even(n))

#print docstring
print(is_even.__doc__)

# parameter vs argument

def  power (a,b):#parameter
    return a**b
print(power(2,3))#argument

#types of arg
#default arg
def  power (a=1,b=1):
    return a**b
print(power(2))


#positional arg
def  power (a,b):
    return a**b
print(power(2,3))


#keyword

def  power (a,b):
    return a**b
print(power(b=2,a=3))

#*args and **kwargs
#*args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function

#*args-allows us to pass a variable number of non-keyword arguments to a function.


def multiply(*args):
    p=1
    for n in args:
        p*=n
    return p

print(multiply(1,2,3))

#**kwargs-kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary

def show(**kwargs):
    for (i,j) in kwargs.items():
        print(i,'-',j)

show(india='delhi',nepal='kathmandu',china='beijing')

#Functions are 1st class citizens-can be passed as argument,return through function,assigned to variable , store in list/dictionary

#assign to variable 
def power(x):
    return x**2
res=power
print(res(4))

#passed as argument
def add(a,b):
    return a+b
def calculate(func,x,y):
    res=func(x,y)
    return res
print(calculate(add,3,4))

#return from function 
def calculate():
    def prod(a,b):
        return a*b

    return prod
res=calculate()
print(res(2,5))

#stored in list/dictionary
l=[1,2,3,4,5,power(7)]
print(l)

lst=[power,add]
print(lst[0](8),lst[1](5,8))

d={
    'power':power,
    'add':add

}
print(d['power'](5),d['add'](6,9))

#del
'''del add
print(add(6,7))'''

'''Benefits of using a Function
Code Modularity
Code Readibility
Code Reusability
Lambda Function
'''

#lambda function 
'''Lambda Function
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

'''
#square of a number
square=lambda x:x**2
print(square(6))

# adding two numbers
sum=lambda x,y:x+y
print(sum(4,5))

# lambda as first class citizen
#assign to variable
sum=lambda x,y:x+y
print(sum(3,8))

#pass as argument 
def solve(square,list):
    result=[]
    for i in list:
        result.append(square(i))

    return result
l=[1,2,3,4,5]
ans=solve(lambda x:x**2,l)
print(ans)

#return from function 
def cal():
    return lambda x:x**3

l=[1,2,3,4,5,6]
result=[]
for i in l:
    f=cal()
    result.append(f(i))
print(result)

'''Diff between lambda vs Normal Function
No name
lambda has no return value(infact,returns a function)
lambda is written in 1 line
not reusable
'''
#check if string has 'a' or not 

check=lambda s: 'a' in s
print(check('abc'))

#print odd or even for a number
p=lambda x: 'even' if x%2==0 else 'odd'
print(p(67))

# lambda + map 
# square the items of a list
print(list(map(lambda x:x**2,[1,2,3,4,5,6,7])))

# odd/even labelling of list items
print(list(map(lambda x:'even'if x%2==0 else 'odd',[1,2,3,4,5,6,7,87])))

# fetch names from a list of dict
users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]
print(list(map(lambda x:x['name'],users)))

# lambda+filter
# numbers greater than 5
print(list(filter(lambda x:x>5,[1,2,3,4,5,6,7,8,9])))

## fetch fruits starting with 'a'
fruits = ['apple','guava','cherry']

print(list(filter(lambda s:s.startswith('a'),fruits)))

#lambda+reduce 

# sum of all item
import functools
print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))

#find min
print(functools.reduce(lambda x,y: x if x<y else y,[2,3,4,1,5,6]))

#sorted + lambda
#sort list 
print(sorted([12,-11,4,-2,-34,5],key=lambda x:abs(x)))

print(sorted(('apple','mangooo','banana'),key = lambda s:len(s)))

d={'c':45,
   'b':67,
   'a':9
   }
print(sorted(d.items(),key=lambda x:x[0]))
print(sorted(d.items(),key=lambda x:x[1]))

#min + lambda

print(min(d.items(),key=lambda x: x[1]))

#max+lambda

print(max(d.items(),key=lambda x:x[0]))