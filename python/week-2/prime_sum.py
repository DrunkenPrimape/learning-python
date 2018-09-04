import math

def sumprimes(numbers):
    
    # Initialize a sum to a start of 0
    sum = 0

    # For each number in the list of numbers
    for number in numbers:
        
        # If the number is greater than 1, do something
        # Else just skip it
        if number > 1:

            # Set a flag to true indicating that we need to add this number
            should_add = True


            # The largest factor of a number cannot be greater 
            # than the square root of the number
            # Since some numbers have irrational roots
            # we apply a ceiling function to get the nearest integer    

            # the plus one is so that our range function doesn't break for 2 -> 2
            divisors = math.ceil(math.sqrt(number)) + 1

            # Run through the list of numbers starting from 2 to the number to 
            # see who can divide it perfectly, ie: the remainder is 0
            for divisor in range(2, divisors): 

                # Skip the current divisor if it is the same as the number
                # as a number is always divisible by itself
                if number == divisor:
                   continue

                if number % divisor == 0:   
                    # If any divisor is perfecly divides 
                    # Set the flag to false and break out
                    # as this number is useless
                    should_add = False
                    break

            if should_add:
                sum += number
    
    return sum

sumprimes([3,3,1,13])
#  19

sumprimes([2,4,6,9,11])
#  13

sumprimes([-3,1,6])
#  0
