'''P23 (**) Extract a given number of randomly selected elements from a list.
The selected items shall be returned in a list.
Example:
* (rnd-select '(a b c d e f g h) 3)
(E D A)'''


def random_permutation(mylist):
    import random

    permutated_list = []            #CREATE AN OUTPUT LIST
    length_list = len(mylist)           #LENGTH OF LIST
    while len(permutated_list) != length_list:      #DO THE PROCESS TILL ALL ELEMENTS ARE TRAVERSED
        for item in range(length_list):                 #ITERATE THROUGH ORIGINAL LIST
            index_of_random = random.randint(0,length_list-1)        #GENERATED NUMBER WILL BE TREATED AS THE INDEX
            if mylist[index_of_random] not in permutated_list:   #IF THE ELEMENT OF THAT INDEX IS NOT ALREADY IN THE LIST
                permutated_list.append(mylist[index_of_random])    #ADD ELEMENT OF THAT INDEX TO THE LIST
        else:                       #IF IT IS ALREADY ADDED,RUN THE PROCESS AGAIN
                continue
    return permutated_list

demo_list= ['a','b','c','d','e','f','g','w']
result = random_permutation(demo_list)
print(f'Original List = {demo_list}\nList after a random permutation = {result}')
