'''P11 (*) Modified run-length encoding.
Modify the result of problem P10 in such a way that if an element has no duplicates it is simply copied into the result list.
Only elements with duplicates are transferred as (N E) lists.

Example:
* (encode-modified '(a a a a b c c a a d e e e e))
((4 A) B (2 C) (2 A) D (4 E))'''




#function to count and pack duplicates into sublists
def count_duplicate(test_list):
    print(f"List before removing duplication = {test_list}")
    previous= test_list[0]                                      #take the first element of the list out
    out=[]                                              #list to save output
    counter=0                                           #counter varaible to count occurance of an element

    for next_element in test_list:                      #iterate through the list

        if previous == next_element:                            #if the elements are equal, increment the counter value
            counter+=1

        else:                              #ELSE PART, FUNCTION CHYA BAHER,LIST RETURN KELYAVAR             #if the elements are not equal and if
            if counter ==1:                                     #the element has occured only once
                out.append(previous)                                # add that element into list without creating sublist

            else:                                       #but if the counter value is greater,
                out.append([counter,previous])                            #create a sublist of the element,how many times it is repeated
            previous=next_element                   #replace the previous with next, to calculate for next element
            counter=1                           #make counter one for other elements
    else:
        out.append(previous)
    return out



my_list = ['a','a','a','b','b','c','c','d','e','e','d','d','f']
res = count_duplicate(my_list)
print("List after packing repeated into sublists = ",res)