'''P09 (**) Pack consecutive duplicates of list elements into sublists.
If a list contains repeated elements they should be placed in separate sublists.

Example:
* (pack '(a a a a b c c a a d e e e e))
((A A A A) (B) (C C) (A A) (D) (E E E E))'''




#function to pack duplicate elements into sublists
def count_duplicate(test_list):

    print(f"List before removing duplication = {test_list}")
    previous= test_list[0]                              #add first element of the list to check with others
    out,sub=[],[]                                                      #output list to return and sublist to create sublist of repeated elements

    for next_element in test_list:                              #iterate through the loop
       if previous == next_element:                         #if previous element is equal to new, add that element into a sublist
           sub.append(previous)

       else:                                            #if the elements are not equal,
            out.append(sub[:])                                              #first add all the elements of sublist into your output list
            previous = next_element                                 #previous element is changed to the non repeated element,to compare with the new element
            sub=[]                                                                              #clear your sublist to save new repeated elements
            sub.append(previous)                                            #the non repeated element is added to the sublist
    else:
        out.append([next_element])                                  #to add the last element to the list


    return out                              #return output list containing sublists of repeated and non repeated elements


my_list = ['a','a','a','b','b','c','c','d','e','e','d','d','f']
res = count_duplicate(my_list)
print("List after packing repeated elements into sublists = ",res)