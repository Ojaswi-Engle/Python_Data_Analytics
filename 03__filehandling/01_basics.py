#writing a file
#case 1: file is not present - write mode
f=open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','w')
f.write('hi how are you?')
f.close()

#write multiline strings 
f=open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','w')
f.write('hello world')
f.write('\nhow are you?')
f.write('\ni am fine')
f.close()

#write if file already present - overwrite
f=open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','w')
f.write('my name is ojaswi')
f.close()

# what if we want to conitnue in existing file -append mode
f=open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','a')
f.write('\ni am 21 years old')
f.close()

#adding multiple lines at a time - use writelines
l=('hello','\nworld','\nhow are you ','\ni am fine')
f=open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','w')
f.writelines(l)
f.close()

#read mode- read whole content in once
f=open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','r')
s= f.read()
print(s)
f.close()
print()

#read n characters
f=open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','r')

data=f.read(10)
print(data)

f.close()


#readline- read line by line
f=open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','r')
print(f.readline(),end='')
print(f.readline(),end='')

f.close()
print('---------------------------------------')

#read a whole file by use of readline()
f=open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','r')
while True:
    data=f.readline()

    if data=='':
        break
    else:
        print(data,end='')
print()

#with - a keyword which by its own closes the file we do not need to close it . 
# write a file by with 
with open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','a') as f:
    f.write('\nI am from Indore')

with open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','r') as f:
    print(f.read())

# chunks of data proceessing for large files
content=['ABCDEFGHIJ','KLMNOPQRST','UVWXYZ1234']
with open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','w') as f:

    f.writelines(content)
with open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','r') as f:
    chunk_size=10
    chunk=f.read(10)
    while True:
        if chunk!='':
            print(chunk,end='***')
            chunk=f.read(10)
        else:
            break

print()
l=['ABCDEFGHIJ','KLMNOPQRST','UVWXYZ1234']
with open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','w') as f:

    f.writelines(l)
with open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','r') as f:
    chunk_size=10
    chunk=f.read(10)
    while len(chunk)>0:
        print(chunk)
        chunk=f.read(10)

#seek  tell function
with open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','r') as f:
    print(f.read(3))
    print(f.tell())

    f.seek(5)
    print(f.tell())
    print(f.read(5))

    f.seek(10)
    print(f.tell())

    

#seek with write 
with open(r'C:\Users\Mohit\OneDrive\Desktop\dsacpp\campusxpython\03__filehandling\sample.txt','w') as f:
    f.write('HELLO WORLD')
    f.seek(0)
    f.write('@#$%')

