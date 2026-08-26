import random
jackpot_num=random.randint(1,100)
attempts=1

n=int(input("enter a number:"))
while n!=jackpot_num:
 if n>jackpot_num:
    print("enter a number less than",n)
 else:
    print("enter a number more than",n)

 n=int(input("enter a number:"))
 attempts+=1
else:
  print('YOU WIN JACKPOT in ',attempts,'ATTEMPTs')