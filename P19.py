#P19 (**) Rotate a list N places to the left.
'''P19 (**) Rotate a list N places to the left.
Examples:
* (rotate '(a b c d e f g h) 3)
(D E F G H A B C)

* (rotate '(a b c d e f g h) -2)
(G H A B C D E F)'''


l = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k']
num= int(input("Places to shift by  = "))
count = []
if num<0:                       #IF GIVEN INDEX IA NEGATIVE,CONVERT INTO ITS EQUIVALENT POSITIVE INDEX
    num+=len(l)
for item in range(num,len(l)):      #ITERATE FROM THE GIVEN INDEX TILL END OF LIST AND ADD IT TO LIST
    count.append(l[item])
for item in range(0,num):           #ITERATE FOR ALL THE ELEMENTS BEFORE THE GIVEN INDEX
    count.append(l[item])           #ADD IT TO LIST

print(f'List after {num} left shifts = {count}')