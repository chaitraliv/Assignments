'''
P39 (*) A list of prime numbers.
Given a range of integers by its lower and upper limit, construct a list of all prime numbers in that range.'''

#CREATE A FUNCTION TO GENERATE PRIME NUMBERS
def prime(num1,num2):
    primenumber=list()                       #LIST TO SAVE PRIME NUMBERS
    if num1>num2 :                           #IF LOWER LIMIT IS HIGHER THAN UPPER LIMIT
        num1,num2 = num2,num1                #SWAP THE NUMBERS
    for num in range(num1,num2+1):           #ITERATE FROM LOWER LIMIT TO UPPER LIMIT
        if num>1 :                           #CONTINUE ONLY FOR POSITIVE INTEGERS
            for i in range (2,num):          #CHECK IF NUMBER IS PRIME
                if num%i == 0:               #IF NON-PRIME,GO FOR NEXT NUMBER
                  break
            else:                            #IF PRIME,SAVE THE NUMBER IN LIST
                    primenumber.append(num)

    return primenumber                       #RETURN THE LIST CONTAINING PRIME NUMBERS



n1=int(input('Give lower limit number = '))
n2 = int(input('Give upper limit number = '))
res = prime(n1,n2)

print(f'Prime numbers between {n1} & {n2} = {res}')
