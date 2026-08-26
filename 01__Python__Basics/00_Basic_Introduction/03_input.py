#input 
first_no=int(input('enter first number:'))
sec_no=int(input('enter second number:'))
result=first_no+sec_no
print(result)   

#type conversion 
#str->int 
print(int('5'))
# float->int 
print(int(6.7))
#int ->string 
print(str(4))
#int -> float 
print(float(45))

print(type(first_no))

#literals 
a=0b1010 #binary
b=100  #decimal 
c=0o310  #octal
d=0x12c  #hexadecimal 
print(a,b,c,d)

#float literals 
print(1.5e3)
print(1.5e-3)

#complex literal 
x=2+3j
print(x,x.real,x.imag)

#string representation
s1='ojaswi'
s2="ojaswi"
char = "C"
multiline_str=""" This is my first learning lecture"""
unicode=u"\U0001f600\U0001F606\U0001F923"
raw_str=r"hello \n world"
print(s1,s2,char,multiline_str,unicode,raw_str)