'''P36 (**) Determine the prime factors of a given positive integer (2).
Construct a list containing the prime factors and their multiplicity.
Example:
* (prime-factors-mult 315)
((3 2) (5 1) (7 1))'''

base_divident=int(input('Enter number to find prime factors = '))
final_out=[]
original=base_divident           #save the original divident,in case needed

#function to calculate prime factors
def prime(divident):
    temp_out = []                                   #temporary list to save the current factor
    for divisor in range(2, divident+1):                          #iterate till the given number
        if divident % divisor ==0:                          #if remainder is zero,it is complete factor
            quotient =divident//divisor                           #save the quotient and use it as the next number
            temp_out.append(divisor)                             #save the number which devides the number as whole
            divident=quotient                              #the quotient will be treated as next number
            return divident,temp_out                                  #return the quotient to be passes as new number and the divisor


while base_divident !=1:                                            #till the divident number doesnt equal 1,run the process
  base_divident,catch_out= prime(base_divident)                                  #get the new divident(quotient) and the divisor and pass the quotuent as new number
  final_out +=catch_out                                                 #add the divisor into output list

previous_element = final_out[0]                             #add the first element of the list to check
counter = 0                                                 #take a variable counter to count instances of a factor
final=[]                                    #final output list

for current_element in final_out:                           #iterate through list containing prime factors
    if current_element == previous_element:                                   #if current element of the list is equal to previously present
        counter+=1                                                  #increment the counter
    else:
        final.append([previous_element,counter])                        #if not,then add the previous element and its count to final list
        counter=1                                               #otherwise for non-repeated factor,set the counter to 1
        previous_element= current_element                               #store current value into previous,so new current value will be checked
else:
    final.append([previous_element,counter])                    #add the last element and its count to final list


print(f'Prime factors of {original}= {final}')