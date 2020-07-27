'''P09 (**) Pack consecutive duplicates of list elements into sublists.
If a list contains repeated elements they should be placed in separate sublists.

Example:
* (pack '(a a a a b c c a a d e e e e))
((A A A A) (B) (C C) (A A) (D) (E E E E))'''




#function to pack duplicate elements into sublists
def count_duplicate(test_list):

    print(f"List before removing duplication = {test_list}")
    previous= test_list[0]                              #add first element of the list to check with others
    out=[]                                                          #output list
    counter=0                                                 #counter to instances of an element

    for next_element in test_list:                                                 #iterate through the list
        if previous == next_element:                                    #check for every element,if it is equal to the one taken out
            counter+=1                      #if so,increament the counter
        else:                                   #if elements are not equal
            out.append([previous * counter])                          #add that element number of times it occured,into a sublist,
            previous=next_element                               #change the base element with next element to check
            counter=1                                       #make the counter 1 for other elements
    return out



my_list = ['a','a','a','b','b','c','c','d','e','e','d','d','f']
res = count_duplicate(my_list)
print("List after packing repeated into sublists = ",res)