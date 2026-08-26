#login credentials
#password checking 

email=input("enter mail_id:")
password=input("enter password:")

if email=='xyz@gmail.com' and password =='12345':
    print("WELCOME")
elif email=='xyz@gmail.com' and password !='12345':
    print("INCORRECT PASSWORD")
    password=input("enter password again:")
    if password=='12345':
        print('WELCOME')
    else:
        print('ERROR')
else:
    print("ERROR")