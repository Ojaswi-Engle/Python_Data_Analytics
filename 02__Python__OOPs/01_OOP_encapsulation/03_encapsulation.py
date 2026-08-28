class Bank:
    def __init__(self):
        self.name="ojaswi"
        self.balance=10000

c1=Bank()
print(c1.balance)

class Bank:
    def __init__(self):
        self.__name="ojaswi"  #cannot be accessed directly from outside of class and not even by c1.__balance
        self.__balance=10000  #_Bank__balance in memory

c1=Bank()
print(c1._Bank__balance)  


#getter and setter
class Bank:
    def __init__(self):
        self.__name="ojaswi"  
        self.__balance=10000  


    def get_balance(self):
        return self.__balance
    
c1=Bank()
print(c1.get_balance())

#setter
class Bank:
    def __init__(self):
        self.__name="ojaswi"  
        self.__balance = 10000  

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print('invalid amount')

c1=Bank()
print(c1.get_balance())
c1.deposit(2000)
print(c1.get_balance())

#static variables = class variable which is common for all objects
class Student:
    college='xyz'

    def __init__(self):
        self.name='Ojaswi'

s=Student()
print(s.college)
print(Student.college)

#private and static
class Student:
    __college='xyz'

    def __init__(self):
        self.name='Ojaswi'
    def get_college(self):
        return Student.__college


s=Student()
print(s.get_college())

#static methods-utility
class Student:
    __college='xyz'

    def __init__(self):
        self.name='Ojaswi'
    @staticmethod
    def get_college():
        return Student.__college

s=Student()
print(Student.get_college())

#collection of objects
class Student:
    __college='xyz'

    def __init__(self,name):
        self.__name=name

    def get_college(self):
        return Student.__college
    def get_name(self):
        return self.__name


s1=Student('a')
s2=Student('b')
s3=Student('c')
s4=Student('d')

l=[s1,s2,s3,s4]
for i in l:
    print(i.get_name())





