""" 
1
12321
1234321
"""
n=int(input("enter a number:"))

for i in range(1,n+1):
    a=1
    for j in range(1,i+1):
        print(a,end='')
        a+=1
    for k in range(i-1,0,-1):
        print(k,end='')

    print()