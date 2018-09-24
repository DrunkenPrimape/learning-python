# def addpoly(polynomial):
#     #Sum = 0
#     polynomial_add = 0
#     for z in polynomial():
#         polynomial_add += polynomial()
#     print(polynomial_add)
#     return(polynomial)

# # defining a function of polynomial
# def polynomial(coefficient, exponent):

#      #Zero polynomial defined
#     polynomial = []

#     #using map function to link coefficient to exponent in a for loop
#     for i in map(coefficient, exponent):

#         #condition for exponent >= 0
#         if exponent >= 0:
#             #nested conditions
#             if exponent[i] <= exponent [i+1]:
#                 return None
#             elif coefficient == 0:
#                 return None
#             else:
#                 sorted(map, reverse = True)
#                 return(map())
#         else:
#             break

#     coefficient_sum = 0
#     # adding polynomials
#     for i in map(coefficient, exponent):
#         if exponent[i] == exponent[i+1]:
#             coefficient_sum += coefficient[i]
#         else:
#             pass

# addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
#  # [(2, 1),(3, 0)]
#  #Explanation: (4x3 + 3) + (-4x3 + 2x) = 2x + 3
# addpoly([(2,1)],[(-2,1)])
#  #  []
#  #Explanation: 2x + (-2x) = 0

#  #polynomial = list
#  # coefficient, exponent
#  #Conditions:
#  # Descending order of exponent - sort
#  # Coefficient != 0
#  # Terms cannot have same exponent
#  # Exponents >= 0

#  #Zero polynomial = []


def addpoly(polynomial1, polynomial2):
    sum = {}

    for (coefficient, exponent) in polynomial1:
        sum[exponent] = coefficient

    for (coefficient, exponent) in polynomial2:
        currentSum = sum.get(exponent)
        if(currentSum == None):
            sum[exponent] = coefficient
        else:
            sum[exponent] = currentSum + coefficient

    keys = sum.keys()
    sortedKeys = sorted(keys, reverse=True)

    nonZeroCoefficients = filter(lambda key: sum.get(key) != 0, sortedKeys)
    result = list(map(lambda key: (sum.get(key), key), nonZeroCoefficients))

    return result


def multpoly(polynomial1, polynomial2):
    sum = {}

    for (coefficient1, exponent1) in polynomial1:
        for (coefficient2, exponent2) in polynomial2:
            newCofficient = coefficient1*coefficient2
            newExponent = exponent1+exponent2
            currentSum = sum.get(newExponent)
            if(currentSum == None):
                sum[newExponent] = newCofficient
            else:
                sum[newExponent] = currentSum+newCofficient

    print(sum)
    keys = sum.keys()
    sortedKeys = sorted(keys, reverse=True)

    nonZeroCoefficients = filter(lambda key: sum.get(key) != 0, sortedKeys)
    result = list(map(lambda key: (sum.get(key), key), nonZeroCoefficients))

    return result


# addpoly([(4, 3), (3, 0)], [(-4, 3), (2, 1)])
# [(2, 1), (3, 0)]
# multpoly([(1, 1), (-1, 0)], [(1, 2), (1, 1), (1, 0)])
# [(1, 3), (-1, 0)]
