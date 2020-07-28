#function to check if a nummber is prime
def check_prime(num):
    for i in range(2, num):
        if num % i == 0:                #check if the required number is prime
            return 0                #0 indicates number is not prime
    return 1


lower = int(input('Please enter lower limit = '))
upper = int(input('Please enter upper limit = '))


#function to get a list two prime numbers that adds up to get a even number in given range
def goldbach(num1,num2):
    for num in range(num1,num2+1):                      #iterate for given range
        if num % 2 == 0:                                        #perform only for even numbers
            for first in range(2,num):                                  #check for a prime number till required number
                if check_prime(first) == 1 and check_prime(num-first) == 1:             #check which prime number pairs can be formed
                    print(f'{num} = {first} + {num-first}')                                 #print the pair for that nuber
                    break

goldbach(lower,upper)