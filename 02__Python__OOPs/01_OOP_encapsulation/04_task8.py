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