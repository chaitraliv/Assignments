#SOLUTION OF P21
'''P21 (*) Insert an element at a given position into a list.
Example:
* (insert-at 'alfa '(a b c d) 2)
(A ALFA B C D)'''


my_list = ['a','b','c','d','e']
#TAKE THE ELEMENT TO BE ADDED AND WHERE TO ADD AS INPUT
elem = input("Enter the data to add = ")
pos= int(input('Where to add  = '))


def add_element(your_list,element,position):
    length = len(your_list)
    out_list = list()

    if position <= len(your_list) and position!= 0:             #GIVEN INDEX SHOULD BE IN RANGE & NOT ZERO
        for item in range(length):
            if position == item+1:                              #WHEN INDICES MATCH,ADD THE ELEMENT INTO RESULT LIST
                out_list.append(element)
            else:
                out_list.append(your_list[item])                #TILL THEN ADD OTHER ELEMENTS
        return (out_list)
    else:
        print('Invalid input ')

result = add_element(my_list,elem,pos)
print(result)