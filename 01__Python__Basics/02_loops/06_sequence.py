""" find the sum of following sequence 
1/1!+2/2!+3/3!..................n terms
"""

n=int(input("enter a  number:"))
sum=0
fact=1
i=1
while i<=n:
    fact*=i
    sum+=(i/fact)
    i+=1

print("sum of following sequence :",sum)