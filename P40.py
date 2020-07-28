'''P40 (**) Goldbach's conjecture.
Goldbach's conjecture says that every positive even number greater than 2 is the sum of two prime numbers.
Example: 28 = 5 + 23. It is one of the most famous facts in number theory that has not been proved to be correct in the general case.
It has been numerically confirmed up to very large numbers (much larger than we can go with our Prolog system).
Write a predicate to find the two prime numbers that sum up to a given even integer.
Example:
* (goldbach 28)
(5 23)'''


#function to check if a nummber is prime
def check_prime(num):
    for i in range(2, num):
        if num % i == 0:                #check if the required number is prime
            return 0                #0 indicates number is not prime
    return 1


number = int(input('Please enter any even number = '))


#function to get two prime numbers that adds up to get a even number
def goldbach(num):
    if num % 2 == 0:                         #check if number is even
        for first in range(2, num):                      #check if any number upto that number is prime,
            if check_prime(first) == 1:                  #if so,grab it as the first prime number,
                second = num - first                                  #the original number minus the prime number will give the second number,
                if check_prime(second) == 1:                 #but check if the 2nd number is prime or not
                    return first, second                              #if yes,return both the numbers
    else:
        return ('Not an even number !')

left,right = goldbach(number)                           #call the goldbach function and catch two prime numbers
print(f'{number} = {left} + {right}')