import random
jackpot_num=random.randint(1,100)
attempts=0

while True:
    n=int(input("enter a number:"))
    attempts+=1

    if n==jackpot_num:
        print('YOU WIN JACKPOT in ',attempts,'attempts')
        break
    elif n>jackpot_num:
        print("enter a number less than ",n)
    elif n<jackpot_num:
        print("enter a number more than ",n)

    