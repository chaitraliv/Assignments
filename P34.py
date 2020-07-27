'''P34 (**) Calculate Euler's totient function phi(m).
Euler's so-called totient function phi(m) is defined as the number of positive integers r (1 <= r < m) that are coprime to m.
Example: m = 10: r = 1,3,7,9; thus phi(m) = 4. Note the special case: phi(1) = 1.
* (totient-phi 10)
4

Find out what the value of phi(m) is if m is a prime number.
Euler's totient function plays an important role in one of the most widely used public key cryptography methods (RSA).
In this exercise you should use the most primitive method to calculate this function (there are smarter ways that we shall discuss later).'''

num = int(input('Enter value of m = '))

#CREATE A FUNCTION TO CALCULATE GCD
def find_gcd(n1,n2):
    while n2!=0:            #BASE CASE IS - gcd(a,0) = a ; SO CHECK TILL N2 IS NOT ZERO
        n1,n2= n2,n1%n2     #ACCORDING TO ALGORITH gcd(a,b)=gcd(b,r) where r=a%b
        find_gcd(n1,n2)     #CONTINUE TO CALCULATE GCD FOR NEW N1 AND N2
    return n1               #WHEN BASE CASE SATISFIES, RETURN N1 WHICH IS GCD

#function to calculate totient of number:
def phi(m):
    count = 0               #counter variable to count co-prime numbers
    for number in range(1,m+1):     #iterate till given number to check gcd
        if find_gcd(number,m)==1:  #check gcd for every number till desires number and number 'm', if co-prime gcd is 1
            count+=1                #if they are co-prime, increment the counter

    return count                   #return the count

output = phi(num)
print(f'totient phi of {num} :- {output}')