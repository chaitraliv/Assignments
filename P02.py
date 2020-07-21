#SOLUTION FOR P02
# Find the last but one box of a list


mylist = ['a','b','c','d','e','d','f','i','j']
length=0

for item in mylist:         #CALCULATE LENGTH OF LIST
    length+=1

count=2                     #INITIATE A COUNTER TO 2 SINCE WE NEED LAST TWO ELEMENTS

print('The last but one element are = ')

for item in mylist:         #ITERATE THROUGH LIST
<<<<<<< HEAD
    if count < length:              #DECREAMENT THE LENGTH TO ELIMINATE THE  ALL ELEMENTS TILL LAST 2
=======
    if count < length:              #DECREAMENT THE LENGTH TO ELIMINATE THE ALL ELEMENTS TILL LAST 2
>>>>>>> ee4f6d50d30eaa31bfdec7b132915827cd95e3e8
        length-=1
    else:                           #LAST TWO ELEMENTS WILL NOT SATISFY ABOVE CONDITION SO PRINT THEM
        print(f"{item}",end =' ')
