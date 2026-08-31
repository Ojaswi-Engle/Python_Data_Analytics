'''Q1:Count number of instances of a class created in Python?
Example: Say Car is any class.

maruti = Car()
bmw = Car()
honda = Car()
So after creating above instances. We want to count how many instances are created of Car class.

For above example no of instances = 3.

Write a program for above problem.'''
#logic 1
class Car:
    pass

def count(*args):
    counter=0
    for i in args:
        if isinstance(i,Car):
            counter+=1
    return counter
maruti=Car()
bmw=Car()
honda=Car()
print(count(maruti,bmw,honda))

#logic 2
class Car:
    __count=0
    def __init__(self):
        Car.__count+=1

    @staticmethod
    def get_count():
        return Car.__count


maruti=Car()
bmw=Car()
honda=Car()
print(Car.get_count())

'''Q-2: Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
The Deck class should have a deal method to deal a single card from the deck
After a card is dealt, it is removed from the deck.
There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
Deck Class

It is class of all possible cards in a deck. Total 52 cards.
Methods - deal() it will take out one card from the deck of cards.
Deck of cards should get shuffeled while creating the deck object.
no of cards remaining in deck - <number> should dsiplay on printing any deck object.
Card class

It is a class of card
Atrributes - suit and value
<suit> of <value> should dsiplay on printing any card object.'''
import random
#card class
class Card:

    def __init__(self,suit,value):
        self.suit=suit
        self.value=value

    def __str__(self):
        return '{} of {}'.format(self.suit,self.value)
#Deck class
class Deck:
    def __init__(self):
        self.suits=['hearts','diamonds','spades','clubs']
        self.values=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.cards=[]
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit,value))
        self.shuffle()

    def shuffle(self):
        if len(self.cards)==52:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards)>0:
            return self.cards.pop()
        else:
            print('No cards left')

    def __str__(self):
        return 'no of cards remaining in deck - {}'.format(len(self.cards))

c=Card('hearts','A')
print(c)
d=Deck()
print(d)
d.deal()
print(d)
for card in d.cards:
    print(card)

'''Q-3: Find the area of a rectangle.
Approach:

The class name should be Rectangle.
The constructor should accept two parameters length and height but you can't pass the values directly to it while creating the constructor. E.g., rectangle = Rectangle(length=10, height=8) <-- you can't do that while creating the instances.
Create a method called area() which has no parameters.
Create a method called is_square() which also has no parameters. Return True if the rectangle is a square otherwise return False.
If you are using a if-else block inside the is_square() method, then use the one-linear syntax.
'''
class Rectangle:
    def __init__(self,length=None,height=None):

        self.length=length
        self.height=height

    def area(self):
        return self.length*self.height

    def is_square(self):
        return self.length==self.height
r=Rectangle()
r.length=12
r.height=4
print(r.area())
print(r.is_square())

'''Q-4: Problem 4
Statement: Write a program that uses datetime module within a class. 
Enter manufacturing date and expiry date of the product. 
The program must display the years, months and days that are left for expiry.'''
from datetime import datetime,date
class Date:
    def __init__(self,exp_date):
        self.exp_date=exp_date

    def display_difference(self):
        curr=date.today()
        exp=datetime.strptime(self.exp_date,'%d-%m-%Y').date()
        if exp<curr:
            print('Product expired')
            return 

        exp_day=exp.day
        exp_month=exp.month
        exp_year=exp.year

        days=exp.day-curr.day
        if days<0:
            if exp.month==1:
                borrow=12
            else:
                borrow=exp.month-1
            l=[1,3,5,7,8,10,12]

            if borrow in l:
                exp_day+=31
            elif borrow==2:
                if (exp_year%400==0 or (exp_year%4==0 and exp_year%100!=0)):
                    exp_day+=29
                else:
                    exp_day+=28
                     
            else:
                exp_day+=30

            days=exp_day-curr.day
            exp_month-=1

        months=exp_month-curr.month

        if months<0:
            exp_month+=12
            exp_year-=1
            months=exp_month-curr.month

        years=exp_year-curr.year

        print('{} days ,{} months ,{} years  are left for expiry'.format(days,months,years))
d1 = Date("02-09-2026")
d1.display_difference()

d2 = Date("30-09-2026")
d2.display_difference()

d3 = Date("28-02-2027")
d3.display_difference()

d4 = Date("29-02-2028")
d4.display_difference()

d5 = Date("28-02-2028")
d5.display_difference()

d6 = Date("30-08-2026")
d6.display_difference()

d7 = Date("31-08-2026")
d7.display_difference()

d8 = Date("01-09-2027")
d8.display_difference()

d9 = Date("28-02-2029")
d9.display_difference()

d10 = Date("29-02-2024")
d10.display_difference()

'''Q-5: Problem 5
Statement: A university wants to automate their admission process. 
Students are admitted based on the marks scored in the qualifying exam.
 A student is identified by student id, age and marks in qualifying exam. 
 Data are valid, if:

Age is greater than 20
Marks is between 0 and 100 (both inclusive)
A student qualifies for admission, if

Age and marks are valid and
Marks is 65 or more
Write a python program to represent the students seeking admission in the university. The details of student class are given below.
'''

class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None 

    def set_student_id(self,student_id):
        self.__student_id=student_id

    def set_marks(self,marks):
        self.__marks=marks

    def set_age(self,age):
        self.__age=age

    def get_student_id(self):
        return  self.__student_id
    
    def get_marks(self):
        return self.__marks
    
    def get_age(self):
        return  self.__age

    def validate_marks(self):
        if self.__marks >=0 and self.__marks<=100:
            return True
        else:
            return False

    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks>=65:
                return True
            else:
                return False
        else:
            return False

s=Student()
s.set_student_id(101)
s.set_marks(65)
s.set_age(21)
print(s.check_qualification())


s.set_student_id(102)
s.set_marks(80)
s.set_age(25)
print(s.check_qualification())

s.set_student_id(103)
s.set_marks(90)
s.set_age(20)
print(s.check_qualification())

s.set_student_id(101)
s.set_marks(64)
s.set_age(21)
print(s.check_qualification())

s.set_student_id(105)
s.set_marks(100)
s.set_age(21)
print(s.check_qualification())

s.set_student_id(106)
s.set_marks(0)
s.set_age(21)
print(s.check_qualification())

'''Q-6: Ice-Cream Scoops and Bowl shop
Create a class Scoop which has one public property flavor and one private proptery price. Take flavor values during object creation.

Create a class Bowl with private prperty scoop_list which will have list of scoopd object.

Create a method add_scoops in Bowl class which will add any no of Scoop objects given as parameter and store it in scoops_list.

Make getter and setter method for price property.

Make a method display to display flavour and price of each Scoop in scoop_list and print total price of the bowl by adding all flavour scoops prices.

Make a method sold in both Scoop class and Bowl class to print no of quantity sold.

Ex.-

choco = Scoop('chocolate')
print(choco)
choco.set_price(100)

berry = Scoop('berry')
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla')
vanilla.set_price(150)

bowl = Bowl()

bowl.add_scoops(choco) # Giving one parameter
bowl.add_scoops(berry, vanilla) # Multiple
# add_scoops should handle both scenerios

print(bowl)

bowl.display()

Scoop.sold()
Bowl.sold()

Output

Flavor - chocolate Price - None
Flavor - berry Price - 120
chocolate
berry
vanilla
Dsiplaying Bowl
Flavor - chocolate Price - 100
Flavor - berry Price - 120
Flavor - vanilla Price - 150
Price of Bowl - 370
3 scoops sold
1 bowls sold
'''
class Scoop:
    __scoop_sold=0

    def __init__(self,flavour):
        self.flavour=flavour
        self.__price=None
        Scoop.__scoop_sold+=1

    def set_price(self,price):
        self.__price=price

    def get_price(self):
        return self.__price

    def __str__(self):
        return 'Flavour - {} Price - {}'.format(self.flavour,self.__price)

    @staticmethod
    def sold():
        print( '{} scoops sold'.format(Scoop.__scoop_sold))

class Bowl:
    __bowl_sold=0

    def __init__(self):
        self.__scoop_list=[]
        Bowl.__bowl_sold+=1

    def add_scoops(self,*args):
        for scoop in args:
            self.__scoop_list.append(scoop)
            print(scoop.flavour)

    def display(self):
        total_price=0
        print('Displaying Bowl')
        for scoop in self.__scoop_list:
            print(scoop)
            scoop_price=scoop.get_price()
            total_price+=scoop_price

        print('Price of Bowl - {}'.format(total_price))

    @staticmethod
    def sold():
        print( '{} bowls sold'.format(Bowl.__bowl_sold))

choco = Scoop('chocolate')
print(choco)
choco.set_price(100)

berry = Scoop('berry')
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla')
vanilla.set_price(150)

bowl = Bowl()

bowl.add_scoops(choco) 
bowl.add_scoops(berry, vanilla) 

bowl.display()

Scoop.sold()
Bowl.sold()




        

    



