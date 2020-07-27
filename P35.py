'''P35 (**) Determine the prime factors of a given positive integer.
Construct a flat list containing the prime factors in ascending order.
Example:
* (prime-factors 315)
(3 3 5 7)'''

divident=int(input('Enter number to find prime factors = '))
final_out=[]
original=divident           #save the original divident,in case needed

#function to calculate prime factors
def prime(num1):
    temp_out = []          #temporary list to save the current factor
    for num in range(2,num1+1):   #iterate till the given number
        if num1 % num ==0:          #if remainder is zero,it is complete factor
            quotient =num1//num          #save the quotient and use it as the next number
            temp_out.append(num)    #save the number which devides the number as whole
            num1=quotient                #the quotient will be treated as next number
            return num1,temp_out      #return the quotient to be passes as new number and the divisor


while divident !=1:              #till the divident number doesnt equal 1,run the process
  divident,catch_out= prime(divident)     #get the new divident(quotient) and the divisor and pass the quotuent as new number
  final_out +=catch_out         #add the divisor into output list
print(f'Prime factors of {original} are {final_out}')