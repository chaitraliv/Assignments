#P17 (*) Split a list into two parts; the length of the first part is given.


mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k']
num= int(input("enter number to slice = "))
first,second = [],[]
count, length = 0, 0

for item in mylist:             #CALCULATE LENGTH OF LIST
    length +=1

if num <= length:               #CHECK IF INPUT IS VALID
    for item in mylist:
        count += 1              #CREATE A COUNTER TO KEEP CHECK ON THE REQUIRED LIMIT
        if count <= num :       #IF COUNT IS IN RANGE OF THE REQUIRED LIMIT,
            first += item       #ADD THE CURRENT ELEMENT INTO A LIST ONE
        else:
            second += item      #IF NOT, ADD INTO SECOND LIST
    print([first]+[second])     #CONCANATE THE 2 STRINGS TO GET THE SLICED LIST

else:
    print('INVALID INPUT !')    #IF GIVEN INDEX IS LARGER THAN LENGTH OF LIST