'''Problem-1: Class inheritence
Create a Bus child class that inherits from the Vehicle class. 
The default fare charge of any vehicle is seating capacity * 100. 
If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. 
so the final fare amount should be 5500. 
You need to override the fare() method of a Vehicle class in Bus class.'''

class Vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity=seating_capacity

    def fare(self):
        return self.seating_capacity*100

class Bus(Vehicle):
    def fare(self):
        total_fare=super().fare()
        total_fare+=0.1*total_fare
        return 'Total Bus fare is: {}'.format(int(total_fare))

b=Bus(50)
print(b.fare())

'''Problem-2: Class Inheritence
Create a Bus class that inherits from the Vehicle class. 
Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.'''

class Vehicle:
    def seating_capacity(self,capacity):
        return capacity


class Bus(Vehicle):
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity)

b=Bus()
print(b.seating_capacity())

'''Problem-3: Write a program that has a class Point. 
Define another class Location which has two objects (Location & Destination) of class Point. 
Also define a function in Location that prints the reflection of Destination on the x axis.'''

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return '({},{})'.format(self.x,self.y)

class Location:
    def __init__(self,Location,Destination):
        self.Location=Location
        self.Destination=Destination

    def reflection_on_x_axis(self):
        return Point(self.Destination.x,-self.Destination.y)

location=Point(2,3)
destination=Point(5,7)
l=Location(location,destination)
print(l.reflection_on_x_axis())

'''Problem-4: Write a program that has an abstract class Polygon. 
Derive two classes Rectangle and Triangle from Polygon and write methods to get 
the details of their dimensions and hence calculate the area'''

from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass 

class Rectangle(Polygon):
    def __init__(self):
         self.length=None
         self.breadth=None

    def setdimensions_rectangle(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

class Triangle(Polygon):
    def __init__(self):
             self.a=None
             self.b=None
             self.c=None

    def setdimensions_triangle(self,a,b,c):
            self.a=a
            self.b=b
            self.c=c
    
    def area(self):
         s=(self.a+self.b+self.c)/2
         return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5

r=Rectangle()
r.setdimensions_rectangle(12,3)
print(r.area())

t=Triangle()
t.setdimensions_triangle(3,4,5)
print(t.area())

'''Problem-5: Write a program with class Bill. 
The users have the option to pay the bill either by cheque or by cash. 
Use the inheritance to model this situation.
'''
class Bill:
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        pass
class Cheque(Bill):
    def pay(self):
        return 'bill paid of {} using Cheque'.format(self.amount)

class Cash(Bill):
    def pay(self):
        return 'bill paid of {} using Cash'.format(self.amount)

c=Cheque(120000)
print(c.pay())
ch=Cash(78899)
print(ch.pay())

#imp concept
class P:
    def show(self):
        return self.x

class C(P):
    def __init__(self):
        self.x=12

    def show(self):
        return super().show() #P.show(c)

c=C()
print(c.show()) #C.show(c)
p=P()
p.show()


'''Q-6: FlexibleDict
As of now we are accessing values from dictionary with exact keys. Now we want to amend accessing values functionality. 
if a dict have key 1 (int) the even if we try to access values by 
giving '1' (1 as str) as key, we should get the same result and vice versa.

Write a class FlexibleDict upon builtin dict class with above required functionality.

Hint- dict[key] => dict.__getitem__(key)

Ex.
fd = FlexibleDict()
fd['a'] = 100
print(fd['a']) # Like regular dict

fd[5] = 500
print(fd[5]) # Like regular dict

fd[1] = 100
print(fd['1']) # actual Key is int but still trying to access through str key.
fd['1'] = 100
print(fd[1])
Output:
100
500
100
100'''

class FlexibleDict(dict):
    def __getitem__(self,key):
        if key in  self:
            return super().__getitem__(key)
        else:
            if isinstance(key,str):
                return super().__getitem__(int(key))

            else:
                return super().__getitem__(str(key))

fd=FlexibleDict()
fd[1]=100
print(fd['1'])

print(fd['a'])
