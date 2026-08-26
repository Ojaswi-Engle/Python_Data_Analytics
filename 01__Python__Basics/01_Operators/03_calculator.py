fnum=float(input("enter first number:"))
snum=float(input("enter second number:"))
op=input("enter operation to be performed:")

if op=='+':
    print(fnum+snum)
elif op=='-':
    print(fnum-snum)
elif op=='*':
    print(fnum*snum)
else :
    print(fnum/snum)