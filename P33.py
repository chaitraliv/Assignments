'''P33 (*) Determine whether two positive integer numbers are coprime.
Two numbers are coprime if their greatest common divisor equals 1.
Example:
* (coprime 35 64)'''


num1 = int(input('enter first number = '))
num2 = int(input('enter second number = '))

#CREATE A FUNCTION TO CALCULATE GCD
def find_gcd(n1,n2):
    while n2!=0:            #BASE CASE IS - gcd(a,0) = a ; SO CHECK TILL N2 IS NOT ZERO
        n1,n2= n2,n1%n2     #ACCORDING TO ALGORITH gcd(a,b)=gcd(b,r) where r=a%b
        find_gcd(n1,n2)     #CONTINUE TO CALCULATE GCD FOR NEW N1 AND N2
    return n1               #WHEN BASE CASE SATISFIES, RETURN N1

res= find_gcd(num1,num2)    #CALL THE FUNCTION AND PASS TWO NUMBERS
if res==1:                  #IF THE RESULTANT GCD IS ONE, NUMBERS ARE CO-PRIME
    print(f'{num1} & {num2} are co-prime')
else:                       #IF GCD IS OTHER THAN 1,NUMBERS ARE NOT CO-PRIME
    print(f'{num1} & {num2} are not co-prime')