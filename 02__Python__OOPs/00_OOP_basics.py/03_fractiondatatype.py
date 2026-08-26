class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d

    def __str__(self):
        return'{}/{}'.format(self.num,self.den)

    def __add__(self,others):
        res_num=self.num*others.den+others.num*self.den
        res_den=self.den*others.den
        return '{}/{}'.format(res_num,res_den)
    def  __sub__(self,others):
        res_num=self.num*others.den-others.num*self.den
        res_den=self.den*others.den
        return '{}/{}'.format(res_num,res_den)
    def __mul__(self,others):
        res_num=self.num*others.num
        res_den=self.den*others.den
        return '{}/{}'.format(res_num,res_den)

    def __truediv__(self,others):
        res_num=self.num*others.den
        res_den=self.den*others.num
        return '{}/{}'.format(res_num,res_den)
    
    def convert(self):
        return self.num/self.den

f=Fraction(1,2)
print(f)
f1=Fraction(1,3)
f2=Fraction(1,4)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)

print(f.convert())

    
