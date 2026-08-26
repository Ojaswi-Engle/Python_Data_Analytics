#1  Print the given strings as per stated format.
#Given strings:"Data" "Science" "Mentorship" "Program" 
#"By" "CampusX" 
print('Data','Science','Mentorship','Program','By','CampusX',sep="-")

#2  Write a program that will convert celsius value to fahrenheit.

celsius=float(input("Enter temperature in celsius:"))
fahren=1.8*celsius+32
print(celsius,"* in fahrenheit = ",fahren)

#3 Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print("Before swapping : num1 = ",num1," and num2 = ",num2)
temp=num1
num1=num2
num2=temp

print("After swapping : num1 = ",num1," and num2 = ",num2)

#4  Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

x=complex(input("Enter first coordinate:"))
y=complex(input("Enter second coordinate:"))

dist=((x.real-y.real)**2 + (x.imag-y.imag)**2)**0.5

print("Distance between ",x," and ",y," = ",dist)

#5 - Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

p=float(input("Enter principle amount :"))
r=float(input("Enter rate :"))
t=float(input("Enter time :"))

SI=(p*r*t)/100

print("Simple interest:","\nprinciple = ",p,"\nrate = ",r,"\ntime = ",t,"\nans = ",SI)

#6  Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
#For example: Input: heads -> 4 legs -> 12
#Output: dogs -> 2 chicken -> 2

heads=int(input("enter number of heads:"))
legs=int(input("enter number of legs:"))

if legs %2!=0 or 2*heads>legs or legs>4*heads:
    print('invalid input')
else:
    dogs=0.5*legs-heads
    chickens=2*heads-0.5*legs
    print("number of dogs:",int(dogs))
    print("number of chickens:",int(chickens))


#7 Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
n=int(input("enter a number:"))

sum_ofsquares=n*(n+1)*(2*n+1)//6

print("sum of squares = ",sum_ofsquares)

#8 Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

t1=int(input("enter first term:"))
t2=int(input("enter second term:"))
n=int(input("enter number of terms:"))

nth_term=t1+(n-1)*(t2-t1)
print(n,"th terms is ",nth_term)

#9  Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

n1=int(input("enter numerator of first fraction:"))
n2=int(input("enter numerator of second fraction:"))
d1=int(input("enter denominator of first fraction:"))
d2=int(input("enter denominator of second fraction:"))

sum=(n1*d2+n2*d1)/(d1*d2)
print(n1,"/",d1," + ",n2,"/",d2,"=",sum)

#10 Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
#Input:
#Dimensions of the milk tank
#H = 20cm, L = 20cm, B = 20cm
#Dimensions of the glass
#h = 3cm, r = 1cm

H=float(input("enter height of milk tank:"))
L=float(input("enter width of milk tank:"))
B=float(input("enter breadth of milk tank:"))

h=float(input("enter height of glass :"))
r=float(input("enter radius of glass:"))

vol_tank=H*L*B
vol_glass=3.14*(r**2)*h

print("Number of glass of milk = ",int(vol_tank//vol_glass))



