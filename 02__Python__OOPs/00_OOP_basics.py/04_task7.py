'''Q-1: Rectangle Class
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

Eg. After making above classes and methods, on executing below code:-

my_rectangle = Rectangle(3 , 4)
my_rectangle.display()
Output:

The length of rectangle is:  3
The width of rectangle is:  4
The perimeter of rectangle is:  14
The area of rectangle is:  12

'''

class Rectangle:
    def __init__(self,length,width):
        self.l=length
        self.w=width
    def perimeter(self):
        p=2*(self.l+self.w)
        return p
    def area(self):
        a=self.l*self.w
        return a
    def display(self):
        print('The length of rectangle is:',self.l)
        print('The width of rectangle is: ',self.w) 
        print('The perimeter of rectangle is:',self.perimeter())
        print('The area of rectangle is:',self.area())

my_rectangle=Rectangle(3,4)
my_rectangle.display()

'''Q-2: Bank Class
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details. Give the complete code for the BankAccount class.
Eg. After making above classes and methods, on executing below code:-

newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(700)

newAccount.Deposit(1000)

newAccount.display()
Output:

Account Number :  2178514584
Account Name :  Mandy
Account Balance :  3100 ₹'''

class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance

    def Deposit(self,amount):
        self.balance+=amount

    def Withdrawal(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print('Insufficient balance')

    def bankFees(self):
        self.balance=self.balance-0.05*self.balance

    def display(self):
        print('Account Number : ',self.accountNumber)
        print('Account Name : ',self.name)
        print('Account Balance  : ',self.balance,'₹')

newAccount = BankAccount(2178514584, "Mandy" , 2800)
newAccount.Withdrawal(700)

newAccount.Deposit(1000)

newAccount.display()

'''Q-3:Computation class
Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.

Create a method called Factorial() which allows to calculate the factorial of an integer n. Integer n as parameter for this method

Create a method called naturalSum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.

Create a method called testPrime() in the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.

Create a method called testPrims() allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only 1 as their common divisor. Eg. 4 and 9 are prime to each other.

Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

Create a static listDiv() method that gets all the divisors of a given integer on new list called Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.


'''

class Computation:

    def __init__(self):
        pass


    def Factorial(self,n):
        fact=1
        for i in range(1,n+1):
            fact*=i
        return fact

    
    def naturalSum(self,n):
        total=0
        for i in range(1,n+1):
            total+=i
        return total

    
    def testPrime(self,n):
        if n<=1:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True

        
    def testPrims(self,n,m):
        for i in range(2,min(n,m)+1):
            if n%i==0 and m%i==0:
                return False
        else:
            return True

    def tableMult(self,n):
        for i in range(1,11):
            print(n,' x ',i,'=',n*i)


    def allTablesMult(self):
        for i in range(1,10):
            for j in range(1,11):
                print(i,' x ',j,'=',i*j)
            print()


    def listDiv(self,n):
        Ldiv=[]
        for i in range(1,n+1):
            if n%i==0:
                Ldiv.append(i)
        return Ldiv

    
    def listDivPrim(self,n):
        l=[]
        for i in range(1,n+1):
            if n%i==0 and self.testPrime(i) :
                l.append(i)
        return l

c=Computation()
print(c.Factorial(5))

print(c.naturalSum(10))

print(c.testPrime(7))

print(c.testPrims(4,9))

c.tableMult(5)

c.allTablesMult()

print(c.listDiv(12))

print(c.listDivPrim(60))

'''Q-4: Build flashcard using class in Python.
Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.

Example 1:

Approach:

Create a class named FlashCard.
Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
Now randomly choose a pair from fruits by using random module and store the key in variable fruit and value in variable color.
Now prompt the user to answer the color of the randomly chosen fruit.
If correct print correct else print wrong.
Output:

welcome to fruit quiz
What is the color of Strawberries
pink
Correct answer
Enter 0, if you want to play again: 0
What is the color of watermelon
green
Correct answer
Enter 0, if you want to play again: 1'''

import random
class FlashCard:

    def __init__(self):
        self.d={'Banana':'yellow','Apple':'red','Strawberry':'pink','Cherry':'red'}
        print('Welcome to fruit quiz')
        

    def question(self):
        
        fruit,color=random.choice(list(self.d.items()))
        print('what is the color of ',fruit,'?')
        user_input=input()
        if color==user_input:
            print('correct answer')
        else:
            print('wrong answer')
        n=int(input('Enter 0,if you want to play again:'))
        if n==0:
            self.question()
        else:
            return
quiz=FlashCard()
quiz.question()

'''Q-5: Problem 5 based on OOP Python.
TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is 
identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:

eligibility criteria:
if experience is more than 3 years, average feedback should be 4.5 or more
if experience is 3 years or less, average feedback should be 4 or more
he/she should posses the technology skill for the course
Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.

Note:

Consider all instance variables to be private and methods to be public.
An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.
Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.
'''

class TechWorld:
    def __init__(self,name,experience,technology_skills,avg_feedback):
        self.name=name
        self.experience=experience
        self.technology_skills=technology_skills
        self.avg_feedback=avg_feedback

    def check_eligibility(self):
        if (self.experience >3 and self.avg_feedback>=4.5) or (self.experience <=3 and self.avg_feedback>=4):
            return True
        else:
            return False
    def allocate_course(self,technology):
        if technology in self.technology_skills :
            return True
        else:
            return False

i1=TechWorld('ojaswi',5,['python','c++'],5.5)
i2=TechWorld('mohit',2,['r','c++'],4)
i3=TechWorld('ruchi',1,['c#','golang'],4.5)
i4=TechWorld('shanu',3,['python','c'],3.5)
print(i1.check_eligibility())
print(i1.allocate_course('python'))
print(i2.check_eligibility())
print(i2.allocate_course('c#'))
print(i3.check_eligibility())
print(i3.allocate_course('golang'))
print(i4.check_eligibility())
print(i4.allocate_course('c++'))


















