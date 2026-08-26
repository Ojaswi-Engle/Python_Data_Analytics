# minimum of 3 numbers

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if a<b and a<c:
    print(a," is minimum")
elif b<a and b<c:
    print(b," is minimum")
else:
    print(c," is minimum")