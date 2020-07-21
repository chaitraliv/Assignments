#P18 (**) Extract a slice from a list.
#Given two indices, I and K, the slice is the list containing the elements between the I'th and K'th element of the original list (both limits included). Start counting the elements with 1


mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k']
low = int(input('Enter lower slicing index = '))
up = int(input('Enter upper slicing index = '))
count,length = 0, 0         #2 COUNTERS FOR INDEX AND LENGTH OF LIST
out = []                    #TO SAVE OUTPUT

for item in mylist :        #CALCULATE LENGTH OF LIST
    length +=1

if low and up < length:     #CONTINUE ONLY IF LIMITS ARE WITHIN LENGTH OF LIST
    for element in mylist:
        count += 1
        if  count in range(low, up+1):          #IF THE COUNTER IS IN BETWEEN THE GIVEN LIMITS
            out += element                      #SAVE THAT ELEMENT

    print(out)
else:
    print('PLEASE ENTER A VALID RANGE !')