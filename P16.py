
mylist = ['a', 'b', 'c', 'd', 'e']
num= int(input(" Enter the kth position = "))

length, count,i =0,0,1
sort=[]               #CREATE A LIST TO SAVE OUTPUT

for element in mylist:              #CALCULATE LENGTH OF LIST
    length+=1

if num<=length:                      #CHECK IF INPUT IS IN RANGE OF LENGTH OF THE LIST
    for item in mylist:
        count+=1
        if count == i*num:          #CHECK IF INDEX OF CURRENT ELEMENT IS IN MULTIPLE OF THE REQUIRED INDEEX
            i+=1
        else:
           sort += item             #IF NOT ADD THAT ELEMENT(IE. REMAINING ALL)TO LIST
    print(sort)
else:
    print('INVALID OUTPUT !')
