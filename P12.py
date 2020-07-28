

mylist = [['a', 'a', 'a'], ['b', 'b'], ['c', 'c'], 'd', ['e', 'e'], ['d', 'd'], 'f']

#Function to unpack the packed list,based on length of every element
def unpack_list(packed_list):
    unpacked_list = []                                      #output list
    for element in packed_list:                                         #traverse through each element of the list,if the element is a sublist
        if len(element) > 1:                            #means its length is not one, so traverse through it to unpack
            for every_element in element:
                unpacked_list.append(every_element)                                 #unpack all the elements of sublist into output list
        else:
            unpacked_list.append(element)                       #if the element is not a sublist,add it into output list

    return unpacked_list                            #return the unpacked list


print(f'The packed list is = {mylist}')
print(f'\nThe unpacked list is = {unpack_list(mylist)}')