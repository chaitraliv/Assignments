'''P10 (*) Run-length encoding of a list.
Use the result of problem P09 to implement the so-called run-length encoding data compression method.
Consecutive duplicates of elements are encoded as lists (N E) where N is the number of duplicates of the element E.

Example:
* (encode '(a a a a b c c a a d e e e e))
((4 A) (1 B) (2 C) (2 A) (1 D)(4 E))'''




#function to pack duplicate elements into sublists
def count_duplicate(test_list):
    print(f"List before removing duplication = {test_list}")
    previous= test_list[0]                                  #add first element of the list to check with others
    out=[]                                                               #output list
    counter=0                                               #counter to instances of an element

    for next_element in test_list:                                  #iterate through the list
        if previous == next_element:                                #check for every element,if it is equal to the one taken out
            counter+=1                                                  #if so,increament the counter
        else:                                                                    #if elements are not equal
            out.append([counter,previous])                                      #add that element number of times it occured,into a sublists
            previous=next_element                                               #change the base element with next element to check
            counter=1                                                       #make the counter 1 for other elements
    return out



my_list = ['a','a','b','b','c','c','d','e','e','d','d','f']
res = count_duplicate(my_list)
print("List after packing repeated into sublists = ",res)