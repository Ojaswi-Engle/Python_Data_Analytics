'''While working with Python tuples, we can have a problem in which we need to perform concatenation
 of records from the similarity of initial element. 
 This problem can have applications in data domains such as Data Science.

'''
#logic 1
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
result=[]
check=[]

for i in range(len(test_list)):
    if test_list[i][0] not in check:
        temp=set(test_list[i])
        check.append(test_list[i][0])

        for j in range(i+1,len(test_list)):
            if test_list[j][0]==test_list[i][0]:
                temp.update(test_list[j])
        result.append(tuple(sorted(temp)))

print(result)

#logic 2
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
result=[]
d={}

for (i,j) in test_list:
    if i not in d:
        d[i]=[]
    d[i].append(j)

for (i,j) in d.items():
    result.append((i,*j))

print(result)

'''Q2: Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.
For eg.

The original tuple : (1, 5, 7, 8, 10)
Resultant tuple after multiplication : 

(1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

output-(5, 40, 91, 136, 80)

'''
t=(1,5,7,8,10)
result=[]

for i in range(len(t)):
    add=0
    
    if i==0:
        add=t[i]*t[i+1]
    elif i==len(t)-1:
        add=t[i]*t[i-1]
    else:
        add=t[i]*(t[i-1]+t[i+1])
    result.append(add)
print(tuple(result))

'''Q3: Check is tuples are same or not?
Two tuples would be same if both tuples have same element at same index

t1 = (1,2,3,0)
t2 = (0,1,2,3)

t1 and t2 are not same

'''
t1 = (1,2,3,0)
t2 = (0,1,2,3)
#logic 1
if len(t1)!=len(t2):
    print("not same")
else:
    for i in range(len(t1)):
        if t1[i]!=t2[i]:
            print('not same')
            break

    else:
        print('same')
    


#logic 2
if len(t1)!=len(t2):
    print("not same")
else:
    for (i,j)  in zip(t1,t2):
        if i!=j:
            print('not same')
            break
    else:
        print('same')

'''Count no of tuples, list and set from a list
list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

Output:

List-2
Set-2
Tuples-1
'''

list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

s=0
l=0
t=0
for i in list1:
    if type(i)==list:
        l+=1
    elif type(i)==set:
        s+=1
    elif type(i)==tuple:
         t+=1
print('list - ',l)
print('tuple - ',t)
print('set - ',s)

'''Q5: Shortlist Students for a Job role
Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

Show every students record in form of tuples if matches all required criteria.

It is assumed that there will be only one primry skill.

If no such candidate found, print No such candidate

Input:

Enter No of records- 2
Enter Details of student-1
Enter Student name- Manohar
Enter Higher Education- B.Tech
Enter Primary Skill- Python
Enter Year of Graduation- 2022
Enter Details of student-2
Enter Student name- Ponian
Enter Higher Education- B.Sc.
Enter Primary Skill- C++
Enter Year of Graduation- 2020

Enter Job Role Requirement
Enter Skill- Python
Enter Higher Education- B.Tech
Enter Year of Graduation- 2022
Output

('Manohar', 'B.tech', 'Python', '2022')

'''
record=[]
required=()
n=int(input('Enter No of records-'))

for i in range(n):
    temp=()
    print('Enter details of student-',i+1)
    name=input('Enter Student name-')
    temp+=(name,)
    higher_ed=input('Enter Higher Education-')
    temp+=(higher_ed,)
    prim_skill=input('Enter Primary Skill-')
    temp+=(prim_skill,)
    grad_year=input('Enter Year of Graduation-')
    temp+=(grad_year,)

    record.append(temp)
print('Enter Job Role Requirement-')

r_higher_ed=input('Enter Higher Education-')
required+=(r_higher_ed,)
r_skill=input('Enter Skill-')
required+=(r_skill,)
r_grad_year=input('Enter Year of Graduation-')
required+=(r_grad_year,)

found=False
for i in record:
    if i[1:]==required:
        print(i)
        found=True
if not found:
    print('no such candidate')
    
