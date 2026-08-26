''''''

#logic 1

test_dict={'CampusX':[5,7,9,4,0],'is':[6,7,4,3,3],'Best':[9,9,6,5,5]}
l=list(test_dict.items())
max_key=l[0][0]
max_value=len(set(l[0][1]))

for i in range(1,len(l)):
    temp=len(set(l[i][1]))
    if temp>max_value:
        max_value=temp
        max_key=l[i][0]
print(max_key)

#logic 2
test_dict={'CampusX':[5,7,9,4,0],'is':[6,7,4,3,3],'Best':[9,9,6,5,5]}
keys=list(test_dict.keys())
values=list(test_dict.values())

max_=0

max_value=len(set(values[0]))
for i in  range(1,len(values)):
    temp=len(set(values[i]))

    if temp>max_value:
        max_value=temp
        max_=i
print(keys[max_])

#logic 3
test_dict={'CampusX':[5,7,9,4,0],'is':[6,7,4,3,3],'Best':[9,9,6,5,5]}
l=list(test_dict.items())
max_value=len(set(l[0][1]))
max_key=l[0][0]

for (i,j) in l:
    if len(set(j))>max_value:
        max_value=len(set(j))
        max_key=i
print(max_key)


''''''

str='CampusX best for DS'
d={'good':'is the best channel','DS':'Data Science'}

for (i,j) in d.items():
    if i in str:
        str=str.replace(i,j)
print(str)

'''Q3: Convert List to List of dictionaries. Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.
Example 1:

Input:

test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]
Output:

[{'name': 'DataScience', 'id': 3}, {'name': 'is', 'id': 8}]
Example 2:

Input:

test_list = ["CampusX", 10]
key_list = ["name", "id"]
Output:

[{'name': 'CampusX', 'id': 10}]

'''
keys=['name','id']
values=['datascience',3,'is',9,'mohit',89]
result=[]
index=0

for i in range(len((values))//len(keys)):
    d={}
    for key in keys:
        d[key]=values[index]
        index+=1

    result.append(d)
print(result)

''''''
l=[('A',1),('B',2),('C',3)]
d={}

for (i,j) in l:
    d[i]=[j]

print(d)

''''''
d={'c':[10,34,3]}
d=dict(sorted(d.items()))
for (i,j) in d.items():
    d[i]=sorted(j)
print(d)


