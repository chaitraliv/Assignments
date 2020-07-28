'''P11 (*) Modified run-length encoding.
Modify the result of problem P10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as (N E) lists.

Example:
* (encode-modified '(a a a a b c c a a d e e e e))
((4 A) B (2 C) (2 A) D (4 E))'''




#function to pack duplicate elements into sublists
def count_duplicate(test_list):

    print(f"List before removing duplication = {test_list}")
    previous= test_list[0]                              #add first element of the list to check with others
    out,sub=[],[]                                                          #output list and sublist to save repeated elements


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


final = []                                                          #final output element list
my_list = ['a','a','a','b','b','c','c','d','e','e','d','d','f']
res = count_duplicate(my_list)                      #the sublist packed output will be stored in res

#iterate through this rest list,for every element of it(sublist), if the element is appearing only ones,unpack it from sublist
for element in res:
    if len(element) !=1:                                    #if the length of sublist is greater than one,
        final.append(element)                                       #add that element(sublist) into final list

    else:                                                   #if the length of element(sublist) is equal to one
        for single in element:                                          #traverse through that sublist and add that single element into final list
            final.append(single)


print("\nList after packing repeated into sublists =\n",final)