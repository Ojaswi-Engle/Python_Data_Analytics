# Find the length of a given string without using the len() function


s=input("enter a string:")
length=0

for i in s:
    length+=1
print("length of ",s," = ",length)

# Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh

email=input("enter an email_id:")
position=email.find('@')
username=email[:position]
print("username:",username)

# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

s=input("enter a string:")
freq=0
char=input("enter a character:")

while len(char)!=1:
    char=input("enter a single character again:")

else:
    for ch in s:
        if ch==char:
            freq+=1
    print("frequency : ",freq)

# Write a program which can remove a particular character from a string.

s=input("enter a string:")
str=''
char=input("enter a character:")
while len(char)!=1:
    char=input("enter single character only :")

for ch in s:
    if ch!=char:
        str+=ch
print(str)

#palindrome program

'''s=input("enter a string:")
rev=s[::-1]
if s==rev:
    print("palindrome")
else:
    print("not palindrome")'''

s=input("enter a string:")

for i in range(len(s)//2):
    if s[i]!=s[len(s)-1-i]:
        print("not palindrome")
        break

else:
    print("palindrome")

# Write a program to count the number of words in a string without split()

s=input("enter a string:")
count=0
#logic 1
'''for i in range(len(s)):
    if i==0 and s[i]!=' ':
        count+=1
    elif s[i]!=' ' and s[i-1]==' ':
        count+=1
print("words:",count)'''
#logic 2
'''inside=False
for ch in s:
    if ch!=' ' and inside==False:
        count+=1
        inside=True

    elif ch==' ':
        inside=False


print("words:",count)'''

#logic 3
word=''
l=[]
for ch in s:
    if ch!=' ':
        word+=ch
    else:
        l.append(word)
        word=''
l.append(word)
print("words:",len(l))

# Write a python program to convert a string to title case without using the title()
s=input("enter a string:")
word=''
#logic 1
'''for i in range(len(s)):
    if i==0 and s[i]!=' ':
        word+=s[i].upper()
    elif s[i]!=' ' and s[i-1]==' ':
        word+=s[i].upper()
    else:
        word+=s[i]
print(word)'''
#logic2
'''inside=False
for ch in s:
    if ch!=' ' and inside==False:
        word+=ch.upper()
        inside=True
    elif ch==' ':
        inside=False
        word+=ch
    else:
        word+=ch
print(word)'''

#logic 3
'''for ch in s:
    if ch != ' ':
        word+=ch
    else:
        word=word[0].upper()+word[1::]
        print(word,end=' ')
        word=''
else:  
    word=word[0].upper()+word[1::]
    print(word,end=' ')'''

#logic 4
l=s.split()
for word in l:
    word=word[0].upper()+word[1::]
    print(word,end=' ')
        
#wap to convert integer to string 
i=int(input("enter an integer:"))
s=''
digits='0123456789'
while i != 0:
    s=digits[i % 10]+s
    i=i//10
print(s)