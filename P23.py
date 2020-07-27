'''P23 (**) Extract a given number of randomly selected elements from a list.
The selected items shall be returned in a list.
Example:
* (rnd-select '(a b c d e f g h) 3)
(E D A)'''

import random

mylist = ['a','b','c','d','e','f']
num = int(input(" Enter how many elements to extract = "))
random_element_list = []            #CREATE AN OUTPUT LIST
length_list = len(mylist)           #LENGTH OF LIST


if num <= length_list:              #CHECK IF LIST HAS ELEMENTS EQUAL TO THE GIVEN NUMBER
    for item in range(num):         #ITERATE FOR HOW MANY ELEMENTS WE NEED
         index_of_random = random.randint(0,length_list)        #GENERATED NUMBER WILL BE TREATED AS THE INDEX
         random_element_list.append(mylist[index_of_random])    #ADD ELEMENT AT THAT INDEX TO THE LIST
print(random_element_list)

