#SOLUTION FOR P31
#P31 (**) Determine whether a given integer number is prime.

num = int(input('Enter any number = '))

if num >1:                                      #CHECK ONLY FOR POSITIVE INTEGERS
    for i in range (2, num ):
        if (num % i) == 0:                      #IF REMENDER IS ZERO FOR ANY DIVISION,IT IS NOT PRIME
            print('is %d prime -  F' %num)

            break
    else:
            print('is %d prime  - T' % num)      #ELSE IT IS PRIME

else:
    print(num,'is not prime')                   #FOR NEGATIVE NUMBERS