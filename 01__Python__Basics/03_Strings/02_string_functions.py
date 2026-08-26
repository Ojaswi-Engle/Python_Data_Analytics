#string functions 

#len
s='this is hello world'
print(len(s))

#min
print(min(s))

#max
print(max(s))

#sorted
print(sorted(s))

#reverse sort
print(sorted(s,reverse=True))

#capitalize
print(s.capitalize())

#title
print(s.title())

#upper 
print(s.upper())

#lower 
print(s.lower())

#swapcase
print(s.swapcase())

#count
print(s.count('l'))

#find
print(s.find('@'))

#index
print(s.index('i'))

#format
s='this is {} {}'
hello='ojaswi'
world='engle'
print(s.format(hello,world))

#isalpha
print(s.isalpha())

#isdigit
print(s.isdigit())

#isalnum
print(s.isalnum())

#isidentifier - imp note value of variable can be an identifier ? is checked
print(s.isidentifier())

#split
print(s.split('i'))

#join 
print('i'.join(['th', 's ', 's {} {}']))

#replace
print(s.replace('i','#'))

#strip
print('ojaswi            '.strip())