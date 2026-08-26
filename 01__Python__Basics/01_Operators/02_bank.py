menu=input("""WELCOME TO XYZ BANK
              1.PRESS 1 FOR PIN CHANGE
              2.PRESS 2 FOR BALANCE CHECK
              3.PRESS 3 FOR CASH WITHDRAWL
              4.EXIT\n""")

if menu=='1':
    print("pin changed")
elif menu=='2':
    print("current balance")
elif menu=='3':
    print("cash withdrawed")
else:
    print("exited")