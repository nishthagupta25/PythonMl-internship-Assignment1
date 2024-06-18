# Write a python program that calculates the sum of the digits of a given number.
number=int(input("Enter a number :"))
sum=0
while(number>0):
    rem=number%10
    sum=rem+sum
    number=number//10
print("The sum of digits of a given number is",sum)
    

