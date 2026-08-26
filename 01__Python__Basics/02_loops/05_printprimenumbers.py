"""print prime numbers between range 
"""
l=int(input("enter lower range:"))
h=int(input("enter higher range:"))

if l<0 and h<0:
    print('invalid range')
else:
    if l<=0 :
        l=1
    for i in range(l,h+1):
        if i==1:
            continue
        check_prime=True
        for j in range(2,i):
            if i%j==0:
                check_prime=False
                break
            
        if check_prime:
            print(i,end=' ')


