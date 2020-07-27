#SOLUTION FOR P32
'''P32 (**) Determine the greatest common divisor of two positive integer numbers.
Use Euclid's algorithm.
Example:
* (gcd 36 63)
9'''

num1 = int(input('enter first number = '))
num2 = int(input('enter second number = '))

#CREATE A FUNCTION TO CALCULATE GCD
def find_gcd(n1,n2):
    while n2!=0:            #BASE CASE IS - gcd(a,0) = a ; SO CHECK TILL N2 IS NOT ZERO
        n1,n2= n2,n1%n2     #ACCORDING TO ALGORITH gcd(a,b)=gcd(b,r) where r=a%b
        find_gcd(n1,n2)     #CONTINUE TO CALCULATE GCD FOR NEW N1 AND N2
    return n1               #WHEN BASE CASE SATISFIES, RETURN N1

res= find_gcd(num1,num2)    #CALL THE FUNCTION AND PASS TWO NUMBERS
print(F'GCD of {num1} & {num2} = {res}')