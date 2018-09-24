# a. Print first N Fibonacci numbers:
# c. Print an amortization schedule for a loan with a given principal (P) and given interest (R) over a time of (Y) years 

# 2. Generate the following patterns given an input N which is number of rows to print
# (ignore the dots.. but the spacing should look uniform)

# a)
# 1
# 1 1 
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1

# b)
# 1
# 1 .2
# 1 . 2 . 3
# 1 . 2 . 3 . 4
# 1 . 2 . 3 . 4 . 5

# c)
# 1
# 2 . 3
# 4 . 5 . 6
# 7 . 8 . 9 . 10
# 11 12 . 13 . 14 . 15

# d)
#                    1
#              1 .  2 .   1
#            1   3 .  3 .   1
#          1 . 4   6 .   4 .  1

# e)      1     1
#         4 .   5
#         9 .  14
#        16    30  


#SOLUTION:

# 1.a
# 0,1,1,2,3,5,8,13,21....
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8

def fibonacci(n):
    a = 0
    b = 1
    for i in range(0,n):
        c = a + b
        #a = b
        #b = c
        (a,b) = (b,a) 
        (c,b) = (b,c) 
   #     print(c)

#Enter the number
fibonacci(10)

#1.c 
# Principal P 
# Interest R 
# Time Y years

# Simple interest = P*R*Y/100 
# for 1st year, let Simple interest be SI
# Amount = SI + P
# for 2nd year, let Simple interest be SI1
# Amount = SI1 + P

def loan_SI(principal, interest, timePeriod):
    simpleInterest = 0
    Amount = 0
    for time in range(1,timePeriod + 1):

        simpleInterest = (principal*interest*time)/100
        Amount = Amount + simpleInterest + principal
    
     #   print(Amount)

print("Simple")
loan_SI(100 ,0.01 , 10 )

# Compound interest = P*(R/100}^Y 
# for 1st year, let Compound interest be S
# Amount = CI + P
# for 2nd year, let Simple interest be CI1
# Amount = CI1 + P


def loan_CI(principal, interest, timePeriod):
    compoundInterest = 0
    Amount = 0
    for time in range(1,timePeriod + 1):

        compoundInterest = principal*((interest/100)**time)
        Amount = Amount + compoundInterest + principal

#        print(Amount)

#print("Compound")
loan_CI(100 ,0.01 , 10 )

#2.a
# 1
# 1 1 
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1

# 1 loop to print rows but same value
# 1 loop to print columns but same value
# column loop in row loop = nested loop

n = 1
#limit = 5
for i in range(0,limit + 1):
    for j in range(0,i):
  #       print(n, end =" ")  
 #   print(" ")
    
# b)
# 1
# 1 .2
# 1 . 2 . 3
# 1 . 2 . 3 . 4
# 1 . 2 . 3 . 4 . 5

# 1 loop to print rows consecutive numbers
# 1 loop to print prints same numbers
# column loop in row loop = nested loop
#print ( " ")
#limit = 5
#for i in range(1,limit + 1):
#    for j in range(1,i):
    #    print(j, end = " ")
   # print(i)

# c)
# 1
# 2 . 3
# 4 . 5 . 6
# 7 . 8 . 9 . 10
# 11 12 . 13 . 14 . 15

# 1 loop to print the numbers
# 1 loop to print limitations for each row
#print(" ")
limit = 15
for i in range(1, limit + 1):
    for j in range(1,i + 1):
        print(j, end = " ")
    print(" ")