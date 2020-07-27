#SOLUTION FOR P33
'''33 (*) Determine whether two positive integer numbers are coprime.
Two numbers are coprime if their greatest common divisor equals 1.
Example:
* (coprime 35 64)
T'''

num1 = int(input('enter first number = '))
num2 = int(input('enter second number = '))

#FUNCTION TOCHECK IF GIVEN NUMBERS ARE CO-PRIME
def check_coprime(n1,n2):
    gcd = 0                                                 #COUNTER VARIABLE TO CHECK IF THEY ARE CO-PRIME
    if num1 and num2 >=0:                                   #CONTINUE FOR POSITIVE INTEGERS
        for i in range (2,(num1)):
            if (num1 % i) ==0 and (num2 % i) == 0:          #IF THE NUMBERS HAVE A COMMON DIVISOR OTHER THAN 1,
               gcd +=1                                      #INCREMENT COUNTER VARIABLE
        if gcd == 0 :                                       #IF COUNTER IS NOT CHANGED, NUMBERS ARE CO-PRIME
            print("Numbers are co-prime")
        else :                                              #ELSE THE NUMBERS ARE NOT CO-PRIME
            print("Numbers are not co-prime")

    else:
        print("Invalid input")

result = check_coprime(num1,num2)                           #CALL THE FUNCTION
