#P07 (**) Flatten a nested list structure.


flattened_list = []

def flaten(data):
    '''Define a function to determine
    if the type of next element of a list is
     a string or a list'''


    for item in data:
        if type(item) == str:               #IF TYPE IS STRING, ADD IT TO OUTPUT LIST
            flattened_list.append(item)

        elif type(item) == list:            #IF IT IS A LIST(NESTED),AGAIN CALL THE FUNCTION TO SIMPLIFY
            flaten(item)
    return flattened_list

mylist=['a',['b',['c','d'],'e','f']]
flattened_list= (flaten(mylist))        #CALL THE FUNCTION
print(flattened_list)                   #PRINT THE OUTPUT
