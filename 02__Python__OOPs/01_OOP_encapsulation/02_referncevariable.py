class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

  def greet(self):
    if self.country == 'india':
      print('Namaste',self.name)
    else:
      print('Hello',self.name)

p=Person('o','i')
p.gender='male'#if we are trying to access a variable which is not in class then it can be created for that particular object
print(p.gender)

#reference variables= variables which hold the reference of objects,basically it does not store the actual data of obj but instead stores its address 
#pass by refernce 
class Person:
  def __init__(self,name):
    self.name=name
def greet(person):
  print(id(person))
  person.name='mohit'

p=Person('ojaswi')
print(id(p))
print(p.name)
greet(p)  #pass by reference 
print(p.name)

#return reference of object
class Person:
  def __init__(self,name):
    self.name=name
def greet(person):
  p1=Person('Mohit')
  print(id(p1))
  return p1

p=Person('Ojaswi')
p2=greet(p)
print(p2.name)
print(id(p2))

#object is mutable
class Student:
    def __init__(self):
      self.name='Ojaswi'

def change(student):
    student.name='Mohit'
    return student

s=Student()
print(id(s))
s1=change(s)
print(id(s1))
print()