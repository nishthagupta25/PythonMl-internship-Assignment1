# Write a python program that returns the minimum and maximum values in a list of numbers.

list1=[1,2,3,4,5,0,-1,8,-11]
print("the minimum element in list1 :", min(list1))
print("the maximum element in list1 :", max(list1))

#or
min=list1[0]
max=list1[0]
for i in list1 :
    if(i<min):
        min=i
    if(i>max):
        max=i
print("the minimum element in list1 :", min)
print("the maximum element in list1 :", max)


