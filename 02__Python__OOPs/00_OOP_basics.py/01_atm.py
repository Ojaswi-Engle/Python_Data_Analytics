class atm:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input('''                     
                            WELCOME 
                            1.press 1 for pin set
                            2.press 2 for pin change
                            3.press 3 for balance check
                            4,press 4 for withdraw
                            5.press 5 for deposit
                            6.press 6 for exit \n''')
        if user_input=='1':
            #pin set
            self.pin_set()
        elif user_input=='2':
            #pin change
            self.pin_change()
        elif user_input=='3':
            #balance check
            self.balance_check()
        elif user_input=='4':
            #withdraw
            self.withdraw()
        elif user_input=='5':
            #deposit
            self.deposit()
        else:
            exit()
    def pin_set(self):
        user_pin=input("Enter pin:")
        self.pin=user_pin
        user_balance=int(input("Enter balance:"))
        self.balance=user_balance
        print('pin set successfully!')
        self.menu()


    def pin_change(self):
        old_pin=input("Enter old pin :")
        if old_pin==self.pin:
            new_pin=input("Enter new pin:")
            self.pin=new_pin
            print('pin changed successfully!')
        else:
            print('Invalid pin entered!!')
        self.menu()


    def balance_check(self):
        user_pin=input('Enter your pin:')
        if user_pin==self.pin:
            print('Current Balance:',self.balance)
        else:
            print('Wrong pin entered!!')
        self.menu()


    def withdraw(self):
        user_pin=input('Enter pin:')
        if user_pin==self.pin:
            amount=int(input('Enter amount to be withdrawn:'))
            if amount<=self.balance:
                self.balance-=amount
            else:
                print('Invalid amount entered!!')
        else:
            print('Wrong pin entered!!')
        self.menu()


    def deposit(self):
        user_pin=input('Enter your pin:')
        if user_pin==self.pin:
            amount=int(input('Enter amount to be deposited:'))
            self.balance+=amount
        else:
            print('Invalid pin entered!!')
        self.menu()

obj=atm()


        
