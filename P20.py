#SOLUTION FOR P20
'''P20 (*) Remove the K'th element from a list.
Example:
* (remove-at '(a b c d) 2)
(A C D)'''

my_list = ['a','b','c','d','e']
pos= int(input('Element to remove = '))

if pos <= len(my_list):             #CHECK IF INPUT IS IN RANGE
    my_list.pop(pos-1)              #REMOVE THE ELEMENT AT GIVEN INDEX
    print(my_list)                  #PRINT THE LIST
else:
    print('Invalid input ')
