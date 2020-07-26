#DUPLICATION REMOVAL
'''P08 (**) Eliminate consecutive duplicates of list elements.
If a list contains repeated elements they should be replaced with a single copy of the element. The order of the elements should not be changed.

Example:
* (compress '(a a a a b c c a a d e e e e))
(A B C A D E)'''

def remove_duplicate(mylist):
    print(f"List before removing duplication = {mylist}")
    sorted_list=[]                                 #CREATE A LIST TO SAVE OUTPUT
    element_to_check = mylist[0]                       #TAKE OUT FIRST ELEMENT OF THE LIST
    for next_element in range(1,len(mylist)):           #ITERATE FROM THE SECOND ELEMENT OF THE LIST
        if element_to_check == mylist[next_element] and mylist[next_element] not in sorted_list:    #IF THE FIRST AND SECOND ELEMENT ARE EQUAL AND SECOND ELEMENT IS NOT IN OUTPUT LIST
           sorted_list.append(mylist[next_element])           #ADD THAT ELEMENT TO OUR LIST

        else:
            if mylist[next_element] not in sorted_list[-1]:   #IF THE ELEMENTS ARE NOT EQUAL AND THE ELEMENT IS NOT THE LAST ELEMENT ADDED TO THE OUTPUT LIST
                sorted_list.append(mylist[next_element])      #ADD IT TO OUTPUT LIST
            element_to_check=mylist[next_element]                     #TAKE THE ADDED ELEMENT TO CONTINUE THE PROCESS
            continue

    return sorted_list

my_list = ['a','a','b','b','c','c','d','e','e','d','d','f']
res = remove_duplicate(my_list)
print("List after duplicate removal = ",res)