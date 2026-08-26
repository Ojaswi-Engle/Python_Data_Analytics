#dictionary
'''Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

In some languages it is known as map or assosiative arrays.

dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

Characterstics:

Mutable
Indexing has no meaning
keys can't be duplicated
keys can't be mutable items
'''
#create 
d={}
print(d)

#1d or 2d 
d1={'name':'ojaswi','age':20,'branch':'cse'}
d2={'name':'ojaswi',
    'age':20,
    'branch':'cse',
    'subject':{'math':89,'english':90,'DSA':85}}
print(d1)
print(d2)

#mixed keys
d3={(1,2,3):'hi','name':'xyz',45:'done'}
print(d3)

#dict function 
d4=dict([(1,'hi'),(2,'hello'),(3,'world')])
print(d4)
d5=dict({('name','ojaswi'),('age',21),('section','c')})
print(d5)

#duplicate keys
d6={'name':'ojaswi','name':'mohit'}
print(d6)

#mutable keys only

#accessing dictionary
d={'name':'ojaswi',
    'age':20,
    'branch':'cse',
    'subject':{'math':89,'english':90,'DSA':85}}

print(d['name'])
print(d['age'])
print(d['subject'])

print(d['subject']['math'])
print(d['subject']['english'])
print(d['subject']['DSA'])

#get function 
print(d.get('name'))
print(d.get('subject'))
print(d.get('subject').get('math'))
print(d.get('subject').get('english'))

#edit 
d['name']='mohit'
d['age']=34
print(d)


#adding key value pair
d['gender']='male'
d['college']='GLBITM'
print(d)

#del/pop/popitem/clear
#del d
#print(d)

del d['name']
print(d)

d.pop('age')
print(d)

d.popitem()
print(d)

d.clear()
print(d)

#operations 
d={'name':'ojaswi',
    'age':20,
    'branch':'cse',
    'subject':{'math':89,'english':90,'DSA':85}}

print('name' in d)
print('ojaswi' in d)

#loops
for keys in d:
    print(keys,d[keys],sep=' - ')

print()

#functions 
#len/min/max/sorted/reverse sorted

print(len(d))
print(min(d))
print(max(d))
print(sorted(d))
print(sorted(d,reverse=True))

#items/values/keys
print(d.items())
print(d.keys())
print(d.values())

#update
d1={'name':'ojaswi','age':21}
d2={'age':20,'gender':'female'}
d1.update(d2)
print(d1)

#dictionary comprehension 
#print squares of first 10 nums
d={ i:i**2       for i in range(1,11)}
print(d)

#using given dictionary convert distance into miles
distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
d={  i:distances[i]*0.62    for i in distances}
d2={  i:j*0.62      for (i,j) in distances.items()}
print(d)
print(d2)

#using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

d={ i:j     for i ,j in zip(days,temp_C)}
print(d)

#using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
d1={ i:products[i]         for i in products if products[i] >0  }
print(d1)
d2={ i:j    for (i,j) in products.items()   if j>0}
print(d2)

# Nested Comprehension
# print tables of number from 2 to 4
d1={ i:{ j:i*j         for j in range(1,11)}  for i in range(2,5)}
print(d1)
d2={ i:[j*i  for j in range(1,11)]  for i in range(2,5)}
print(d2)
