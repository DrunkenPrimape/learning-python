# # Algorithm 1
# # Defining the greatest common divisor funtion of two numbers
# def gcd(number1,number2):

# # Defining a list of factors for number 1
#     factorOfNumber1 = []
#     for i in range(1, number1 + 1):
#         if (number1 % i) == 0:
#             # if condition is satisfied add the number to the list
#             factorOfNumber1.append(i)
    
# # Defining a list of factors for number 2
#     factorOfNumber2 = []
#     for j in range(1, number2 + 1):
#         if (number2 % j) == 0:
#             factorOfNumber2.append(j)
    
# # Defining a list of common factors for both number 1 and number2
#     commonFactor = []
#     for factor in factorOfNumber1:
#         if factor in factorOfNumber2:
#             commonFactor.append(factor)

# # Returning the right most common factor in the list of common factors
#     print(commonFactor[-1])
#     return(commonFactor[-1])



# # # Algorithm 2
# def gcd1(number1,number2):
#     # Defining aa list of common factors
#     commonFactor = []

#     # Running the for loop
#     for i in range(1, min(number1,number2) + 1):

#         # Checking the divisibility condition
#         if (number1 % i ) == 0 and (number2 % i) == 0:

#             # Adding value to the list if the condition works
#             commonFactor.append(i)

#     print(commonFactor[-1])
# # Return greatest common divisor
#     return(commonFactor[-1])



# # Algorithm 3
# def gcd2 (number1,number2):
#     i = min(number1,number2)
#     while i > 0:
#         if (number1 % i) == 0 and (number2 % i) == 0:
#             #print(i)
#             return(i)
#         else:
#             i = i - 1


# # Algorithm 4 
# def gcd(number1,number2):
#     # Assume number 1 > number 2
#     if number1 < number2:
#         (number1,number2) = (number2,number1)
#     else:
#         difference = number1 - number2
#     return (gcd(max(number2, difference), min(number2, difference)))

# Recursion error taking place


# # Algorithm 5
# def gcd(number1, number2):
#     if number1 < number2:
#         (number1,number2) = (number2,number1)
    
#     while (number1 % number2) != 0:
#         difference = number1 - number2
#         (number1, number2) = (max(number2,difference), min(number2,difference))
#         print(difference, number2)
#     return(number2)

#Test Cases :
#gcd(5,2)
#gcd(120,40)
#gcd(101,2)