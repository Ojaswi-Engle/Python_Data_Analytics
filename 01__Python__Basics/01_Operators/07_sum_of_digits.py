#sum of 3 digit number 

n=int(input("enter a 3 digit number:"))

last_digit = n%10
n=n//10

second_digit=n%10
n=n//10

first_digit=n%10

print("sum of digits : ",first_digit+second_digit+last_digit)

