#P14 (*) Duplicate the elements of a list.


mylist=['a','b','c','c','d','e']
new=[]                      #create a new list
for i in mylist:
    new+=i*2                #duplicate every element of main list and display the new list
print(f'Duplicated list is \n{new}')
