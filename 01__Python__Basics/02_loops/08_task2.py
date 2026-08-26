"""Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
above 20 : 30% 
"""

CTC = float(input("enter salary in lakhs(per year):"))

HRA=0.1*CTC
DA=0.05*CTC
PF=0.03*CTC
if CTC < 5:
    tax=0
elif CTC<=10:
    tax=0.1*CTC
elif CTC<=20:
    tax=0.2*CTC
else:
    tax=0.3*CTC
salary=(CTC-HRA-DA-PF-tax)
in_handmonthlysalary=(salary/12)*100000
print("In hand monthly salary :",in_handmonthlysalary)

#-----------------------------------------------------------------------------------------

""" 
Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
"""
angle1=int(input('enter first angle of triangle:'))
angle2=int(input('enter second angle of triangle:'))
angle3=int(input('enter third angle of triangle:'))

if angle1>0 and angle2>0 and angle3>0 and angle1+angle2+angle3 ==180:
    print("traingle can be formed")
else:
    print("traingle cannot be formed")


"""Problem 3: Write a program that will take user input of cost price and selling price 
and determines whether its a loss or a profit."""

cost_price=float(input("enter cost price(in rupees) :"))
selling_price=float(input("enter selling price(in rupees) :"))

if cost_price>selling_price:
    print("LOSS : ",cost_price-selling_price)
elif cost_price<selling_price:
    print("PROFIT : ",selling_price-cost_price)
else:
    print("NEITHER PROFIT NOR LOSS ")

"""Problem 4: Write a menu-driven program -
cm to ft
km to miles
USD to INR
exit"""

while True:

        menu = input("""ENTER choice for following conversions:
                1.enter 1 for cm -> ft
                2.enter 2 for km -> miles 
                3.enter 3 for USD-> INR
                4.enter 4 for exit\n""")
        if menu=='1':
            cm = float(input("enter value in cms :"))
            ft=0.0328*cm
            print(ft,"fts")
        elif menu=='2':
            km = float(input("enter value in kms :"))
            miles=km*0.621
            print(miles,"miles")
        elif menu=='3':
            USD= float(input("enter value in USD :"))
            INR=94.5*USD
            print(INR,"INR")
        elif menu=='4':
            print("EXIT")
            break
        else:
            print("INVALID input")
            

"""Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34"""


n = int(input("enter  number of terms :"))
a1=0
a2=1
if n<=0:
    print("invalid input")
elif n==1:
    print(a1)

else:
    print(a1,a2,end=" ")

    for i in range(n-2):
      an=a1+a2
      print(an,end=" ")
      a1=a2
      a2=an

""" problem 6 Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: `!`) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5
"""

n=int(input("enter a number :"))
fact=1

for i in range(1,n+1,1):
    fact*=i
print('factorial of ',n ,":",fact)

""" Problem 7 - Reverse a given integer number.
Example:

Input:

76542
Output:

24567

"""
n=int(input("enter a number:"))
rev=0
n1=n
while n != 0:
    last=n%10
    rev=rev*10+last
    n=n//10
print("reverse of ",n1," = ",rev)

"""Problem 8: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, 
then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. 
Print the final result. And don't use for loop to solve this problem.
"""

n=int(input("enter a number:"))
sum=0

i=1
while i<=n:
    if i%5==0:
        i=i+1
        continue
    
    
    if sum+i>300:
        break
    
    sum=sum+i
    i=i+1


print("sum : ",sum)

""""Problem 9: Write a program that keeps on accepting a number from 
the user until the user enters Zero.
Display the sum and average of all the numbers.
"""


sum=0
avg=0
counter=0

while True:
    n=int(input("Enter a number:"))

    if n==0:
        break
    sum=sum+n
    counter=counter+1
if counter==0:
    print("no number entered")
else:
    avg=sum/counter
    print('\nsum of all numbers:',sum)
    print('\navg of all numbers:',avg)

""" problem 10 Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

i=2000
while i<=3200:
    if i%7==0 and i%5!=0:
        print(i,end=",")
    i=i+1

"""Problem 11: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that 
each digit of the number is an even number. 
The numbers obtained should be printed in a space-separated sequence on a single line.
"""
i=1000
while i<=3000:
    n=i
    check=True
    while n!=0:
        d=n%10
        if d%2!=0:
            check=False
            break
        n=n//10
    if check:
        print(i,end=" ")
    i=i+1

""" Problem 11: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
!
The numbers after the direction are steps.

! means robot stop there.

Please write a program to compute the distance from current position after a sequence of movement and original point.

If the distance is a float, then just print the nearest integer.

Example:

Input:

UP 5
DOWN 3
LEFT 3
RIGHT 2
!
Output:

2

"""



current_x=0
current_y=0
original_x=0
original_y=0
while True:
    direction=input() 
    if direction=="!":
        break
    steps=int(input())
    if direction=="UP":
        
        current_y+=steps
        
    elif direction=="DOWN":
        
        current_y-=steps
    elif direction=="LEFT":
       
        current_x-=steps
    elif direction=="RIGHT":
        
        current_x+=steps
    
    

dist=round(((current_x-original_x)**2+(current_y-original_y)**2)**0.5)
print("Distance between (0,0) and (",current_x,",",current_y,") = ",dist)

"""Problem 12:Write a program to print whether a given number is a prime number or not
"""
n=int(input("Enter a number:"))
if n<=1:
    print("neither prime nor composite")
else:
    prime_check=True
    for i in range(2,n):
        if n % i == 0:
            prime_check=False
            break

    if prime_check:
        print("prime")
    else:
        print("not prime")
"""problem 13   Print all the Armstrong numbers in a given range.
Range will be provided by the user
Armstrong number is a number that is equal to the sum of cubes of its digits. 
For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
"""

import math

l=int(input("enter lower range:"))
h=int(input("enter higher range:"))

i=l
while i<=h:
        if i==0:
            print(0,end=" ")
            i=i+1
            continue
        n1=n2=i
        sum=0
        count=0
        
        while n1!=0:
                n1=n1//10
                count+=1
        
        while n2!=0:
                d=n2%10
                sum+=int(math.pow(d,count))
                n2=n2//10
        
        if sum ==i:
                print(i,end=" ")
        i=i+1

"""Problem 14:Calculate the angle between the hour hand and minute hand.
Note: There can be two angles between hands; we need to print a minimum of two. 
Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.
Input:
H = 9 , M = 0
Output:
90
Explanation:
The minimum angle between hour and minute hand when the time is 9 is 90 degress.
"""
import math

H=int(input("enter hour:"))
M=int(input("enter minutes:"))

minute_hand=M*6
hour_hand=H*30+0.5*M

angle1=math.fabs(hour_hand-minute_hand)
angle2=360-angle1

print('angle between minute hand and hour hand :',min(math.floor(angle1),math.floor(angle2)))

"""
Problem 15:Given two rectangles, find if the given two rectangles overlap or not. 
A rectangle is denoted by providing the x and y coordinates of two points: 
the left top corner and the right bottom corner of the rectangle. 
Two rectangles sharing a side are considered overlapping. 
(L1 and R1 are the extreme points of the first rectangle and L2 
and R2 are the extreme points of the second rectangle).
"""
L1_x=int(input("enter x coordinate of left top corner  of first rectangle : "))
L1_y=int(input("enter y coordinate of left top corner  of first rectangle : "))

R1_x=int(input("enter x coordinate of right bottom corner  of first rectangle : "))
R1_y=int(input("enter y coordinate of right bottom corner  of first rectangle : "))

L2_x=int(input("enter x coordinate of left top corner  of second rectangle : "))
L2_y=int(input("enter y coordinate of left top corner  of second rectangle : "))

R2_x=int(input("enter x coordinate of right bottom corner  of second rectangle : "))
R2_y=int(input("enter y coordinate of right bottom corner  of second rectangle : "))

if R1_x < L2_x or R2_y > L1_y or R2_x < L1_x or L2_y < R1_y:
    print(" both rectangles do not overlap each other")
else:
    print(" both rectangles overlap each other")
    



