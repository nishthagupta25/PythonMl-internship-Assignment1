#Write a python program that calculates the factorial of a given number.
num=int(input("Enter any number :"))
factorial =1
if(num<0):
    print("factorial for given number is not possible !!!")
while(num>0):
    factorial=num*factorial
    num=num-1
print("factorial for given number is :",factorial)