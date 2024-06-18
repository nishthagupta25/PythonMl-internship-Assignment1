# Write a python program that generates the first n numbers in the fibonacci sequence
num = int(input("Enter an index till which you want to write fibonacci series : "))
a=0
b=1
print(a)
print(b)

for i in range[0:num-2]:
    c=a+b
    print(c)
    a=b
    b=c

