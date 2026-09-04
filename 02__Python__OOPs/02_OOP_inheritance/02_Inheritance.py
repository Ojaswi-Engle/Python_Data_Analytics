#inheritance code
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def walk(self):
        print('Person is walking')

    def eat(self):
        print('Person is eating')

class Student(Person):
    def study(self):
        print('student is studying')

s=Student('Ojaswi',20)
s.walk()
s.eat()
s.study()
print(s.name)

# child class can inherit = constructor,non-private attribute,non-private methods of parent class 
#if constructor is not present in child class then parent constructor will be executed 
class Phone:
    def __init__(self,name,camera,price):
        self.name=name
        self.camera=camera
        self.price=price
        print('Inside phone constructor')

    def buy(self):
        print('Buying a phone')

class Smartphone(Phone):
    pass
s=Smartphone('Samsung',128,20000)
s.buy()
print(s.name)
print(s.camera)
print(s.price)

#if constructor is  present in child class then it  will be executed 

class Phone:
    def __init__(self,name,camera,price):
        self.name=name
        self.camera=camera
        self.price=price

    def buy(self):
        print('Buying a phone')

class Smartphone(Phone):
    def __init__(self,os,ram):
        self.ram=ram
        self.os=os


s=Smartphone('Android',2)
s.buy()

# child cannot access private atttributes of parent class
class Phone:
    def __init__(self,name,camera,price):
        self.__name=name
        self.camera=camera
        self.price=price
        print('Inside phone constructor')

    def buy(self):
        print('Buying a phone')
    def get_name(self):
        return self.__name
    
class Smartphone(Phone):
    pass
s=Smartphone('Samsung',128,20000)
s.buy()
print(s.get_name())
print(s.camera)
print(s.price)

#method overriding
class Phone:
    def __init__(self,name,camera,price):
        self.name=name
        self.camera=camera
        self.price=price

    def buy(self):     #method buy in child also overrided by child class
        print('Buying a phone')

class Smartphone(Phone):
    def __init__(self,os,ram):
        self.ram=ram
        self.os=os
        print('inside smartphone constructor')

    def buy(self):
        print('buying smartphone')

s=Smartphone('Android',2)
s.buy()
print('------------------------------------------------------------------------------------------------')



#Super function
class Phone:
    def __init__(self,name,camera,price):
        self.name=name
        self.camera=camera
        self.price=price
        print('inside phone constructor')

    def buy(self):     
        print('Buying a phone')

class Smartphone(Phone):
    def __init__(self,os,ram):
        self.ram=ram
        self.os=os
        print('inside smartphone constructor')

    def buy(self):
        super().buy()
        print('buying smartphone')

s=Smartphone('Android',2)
s.buy()
print('------------------------------------------------------------------------------------------------')



#super function
class Phone:
    def __init__(self,name,camera,price):
        self.name=name
        self.camera=camera
        self.price=price
        print('inside phone constructor')

    def buy(self):     
        print('Buying a phone')

class Smartphone(Phone):
    def __init__(self,os,ram,name,camera,price):
        self.ram=ram
        self.os=os
        print('inside smartphone constructor')
        super().__init__(name,camera,price)
        print('inside smartphone constructor')

    def buy(self):
        print('buying smartphone')

s=Smartphone('Android',2,'apple',128,150000)
s.buy()
print(s.name)
print(s.camera)
print(s.price)

#types of inheritance 
#single inheritance 
class Phone:
    def __init__(self,name,camera,price):
        self.name=name
        self.camera=camera
        self.price=price
        print('Inside phone constructor')


    def buy(self):
        print('Buying phone')
class SmartPhone(Phone):
    pass
s=SmartPhone('samsung',128,20000)
print(s.name,s.camera,s.price)
s.buy()

#multilevel inheritance
class Product:
    def review(self):
        print('reviewing product')

class Phone(Product):
    def __init__(self,name,camera,price):
        self.name=name
        self.camera=camera
        self.price=price
        print('Inside phone constructor')
    
    
    def buy(self):
        print('Buying phone') 

class SmartPhone(Phone):
    def buy(self):
        print('buying smartphone') 
        super().buy()    #child can inherit from parent

s=SmartPhone('apple',128,120000)
s.buy() 
s.review()#child can inherit from grandparent 

#hierarchial inheritance 
class Vehicle:
    def __init__(self,number,color,price):
        self.number=number
        self.color=color
        self.price=price
        print('inside vehicle constructor')

    def start(self):
        print('vehicle started')

class Car(Vehicle):
    def __init__(self,name):
        self.name=name
        super().__init__('xy 1234','white',400000)
        print('inside car constructor')


    def speed(self,speed):
        print('speed of car is:',speed)

class Bike(Vehicle):
    def speed(self,speed):
        print('speed of car is:',speed)

c=Car('Breeza')
c.start()
c.speed(67)
print(c.name,c.color,c.price,c.number)

b=Bike('ab 1234','black',150000)
b.start()
b.speed(50)
print(b.color,b.number,b.price)

#multiple inheritance
class Product:
        def __init__(self,quant):
            self.quant=quant
            print('inside Product constructor')
            super().__init__(123,12000,'apple')

        def review(self):
            print('Reviewing product')

        def buy(self):
              print('buying product')
              super().buy()

class Phone:
        def __init__(self,camera,price,brand):
              self.camera=camera
              self.brand=brand
              self.price=price
              print('inside Phone constructor')

        def buy(self):
              print('buying phone')

class SmartPhone(Product,Phone):
        def __init__(self,os,ram):
              self.os=os
              self.ram=ram
              print('inside Smartphone constructor')
              super().__init__(3)

        def buy(self):
              print('buying smartphone')
              super().buy()

s=SmartPhone('IOS',128)
s.buy()
s.review()

#hybrid inheritance
class Grandfather:
      def __init__(self,name,age):
            self.gf_name=name
            self.gf_age=age
            print('inside grandfather constructor')
            super().__init__('priya',40)

class Father(Grandfather):
      def __init__(self,name,age):
            self.f_name=name
            self.f_age=age
            print('inside father constructor')
            super().__init__('kailash',70)
            

class Mother:
      def __init__(self,name,age):
            self.m_name=name
            self.m_age=age
            print('inside Mother constructor')

class Child(Father,Mother):
      def __init__(self,name,age):
            self.c_name=name
            self.c_age=age
            print('inside child constructor')
            super().__init__('aman',42)

c=Child('rohan',12)
print(c.c_name)
print(c.f_name)
print(c.m_name)
print(c.gf_name)


      





