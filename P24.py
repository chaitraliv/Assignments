#SOLUTION FOR P24
'''P24 (*) Lotto: Draw N different random numbers from the set 1..M.
The selected numbers shall be returned in a list.
Example:
* (lotto-select 6 49)
(23 1 17 33 21 37)'''


from random import randint

num = int((input(" Enter How many numbers = ")))            #TAKE REQUIRED INPUT
limit = int(input("Numbers upto = "))                       #TAKE THE LIMIT OF THE SET
count, random_element=1, []                                 #CREATE A COUNTER AND A OUTPUT LIST

while count <= num:                                     #CONTINUE TILL  WE DONT GET THE REQUIRED NUMBER OF RANDOM NUMBER
    element_taken = ((randint(1, limit)))               #SAVE THE RANDOM NUMBER GENERATED
    random_element.append(element_taken)                #CREATE A LIST
    count+=1                                            #INCREMENT THE COUNTER TO KEEP CHECK OF HOW MANY NUMBERS

print(f'Randomly selected elements from the set are = {random_element}')
