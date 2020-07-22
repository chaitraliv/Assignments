#SOLUTION FOR P23
#P22 (*) Create a list containing all integers within a given range.


lower= int(input (' Enter lower limit = '))             #TAKE LOWER AND UPPER LIMIT FROM THE USER
upper= int(input (' Enter upper limit = '))

#FUNCTION TO PRINT DATA BETWEEN 2 LIMITS

def print_data(lower,upper):
    mylist=[]
    for i in range (lower, upper+1) :           #ADD DATA FROM LOWER LIMIT TILL UPPER LIMIT
         mylist.append(i)

    return mylist

result = print_data(lower,upper)                #GIVE THE LIMITS AS INPUT TO FUNCTION
print(result)