#SOLUTION FOR 03


mylist=['a','b','c','d','e']
length, count = 0,0

for element in mylist:                  #Calculate the length of the list
    length+=1

num= int(input("K'th element to be found = "))

if num <= length:
    for item in mylist:                 #iterate through list
        count+=1                        #index of the current item in the list
        if count == num:                #if index of current item is equals input index,print it
            print(f'The {num}th element in the list {mylist} is - \n{item}')

else:
    print('INVALID INPUT !!')