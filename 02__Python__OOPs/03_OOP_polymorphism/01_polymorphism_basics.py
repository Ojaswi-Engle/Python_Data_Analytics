#polymorphism - many forms
#method overloading 
class Shape:
    def area(self,a,b=0):
        if b==0:
            return 3.14*a**2
        else:
            return a*b
s=Shape()
print(s.area(2))
print(s.area(2,3))

#method overriding
class Person:
    def walk(self):
        print('person walks')

class Student(Person):
    def walk(self):
        print('Student walks')

def walk_display(w):
    w.walk()

walk_display(Person())
walk_display(Student())

#operator overloading 
print(2+3)
print('hello'+'world')
print([1,2,3,4]+[5,6,7,8,9])
