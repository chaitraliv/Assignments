#SOLUTION FOR P02
# Find the last but one box of a list


mylist = ['a','b','c','d','e','d','f','i','j']
length=0

for item in mylist:         #CALCULATE LENGTH OF LIST
    length+=1

count=2                     #INITIATE A COUNTER TO 2 SINCE WE NEED LAST TWO ELEMENTS
element=[]
print('The last but one element are = ')

for item in mylist:         #ITERATE THROUGH LIST

    if count < length:              #DECREAMENT THE LENGTH TO ELIMINATE THE ALL ELEMENTS TILL LAST 2

        length-=1
    else:                           #LAST TWO ELEMENTS WILL NOT SATISFY ABOVE CONDITION SO SAVE THEM
        element += item

print(element )

