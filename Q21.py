# Write a python program that counts the occurrences of a specific element in a list

list1=[2,3,4,1,5,2,2,3,1]
print("The occurences of 2 in list1,*METHOD 1* -->",list1.count(2))

#or
count=0
for i in list1:
    if(i==2):
        count=count+1
print("The occurences of 2 in list1,*METHOD 2*--->",count)


