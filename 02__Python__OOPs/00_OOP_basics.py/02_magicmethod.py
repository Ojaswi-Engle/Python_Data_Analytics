#magic methods - str init add sub mul truediv len
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def __str__(self):
        return '{}'.format(self.marks)
    def __add__(self,others):
        return self.age+others.age
    def __len__(self):
        return len(self.marks)


s1=Student('Ojaswi', 21 ,[90, 78 ,89,97])
s2=Student('Mohit',22,[98,99,95,79])
s3=Student('Ruchi',24,[78,90,76,99])
print(s1)
print(s1+s2)
print(len(s1))


