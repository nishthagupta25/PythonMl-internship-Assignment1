# Write a program that acts as a simple calculator. It should take two
# numbers and an operator (+, -, *, /) as input and print the result.

num1=int(input("enter your first number :"))
num2=int(input("enter your second number :"))
operator=input("enter the operator:")
if(operator=='+'):
    ans=num1+num2
if(operator=='-'):
    if(num1>num2):
        ans=num1-num2
    else:
        ans=num2-num1 
if(operator=='*'):
    ans=num1*num2
if(operator=='/'):
    ans=num1/num2
print("the result is :",ans)   