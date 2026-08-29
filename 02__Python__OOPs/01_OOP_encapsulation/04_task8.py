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

