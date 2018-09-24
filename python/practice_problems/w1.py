# Question 1
def g(x):
    (q,d) = (1,0)
    while q <= x:
        (q,d) = (q * 10,d + 1)
    return(d)

#print(g(31415927))

# SOLUTION:
# x = 31415927
# (q,d) = (1,0)
# while 1 <= 31415927
    # (q,d) = (1 * 10, 0 + 1) : 1
    # (q,d) = (10,1)
# while 10 <= 31415927
    # (q,d) = (10 * 10, 1 + 1) : 2
    # (q,d) = (100,2)
# while 100 <= 31415927
    # (q,d) = (100 * 10, 2 + 1) : 3
    # (q,d) = (1000,3)
# while 1000 <= 31415927
    # (q,d) = (1000 * 10, 3 + 1) : 4
    # (q,d) = (100,4)
# while 10000 <= 31415927
    # (q,d) = (10000 * 10, 4 + 1) : 5
    # (q,d) = (100,5)
# while 100000 <= 31415927
    # (q,d) = (100000 * 10, 5 + 1) : 6
    # (q,d) = (100,6)
# while 1000000 <= 31415927
    # (q,d) = (1000000 * 10, 6 + 1) : 7
    # (q,d) = (100,7)
# while 1000000 <= 31415927
    # (q,d) = (10000000 * 10, 7 + 1) : 1
    # (q,d) = (100,8)
# while 10000000 > 31415927
    # (q,d) = (10 * 10, 1 + 1) : 1 False
    # (q,d) = (100,2)   False
#return (8)

#Question 2
def h(m,n):
    ans = 0
    while (m >= n):
        (ans,m) = (ans + 1, m - n)
        print(ans)
    return(ans)

#print(h(231,8))

#SOLUTION:
# m = 231 
# n = 8
# ans = 0
# while (231 >= 8)
# (ans,m) = (0 + 1, 231 - 8) : 1
# (ans,m) = (1,223)
# while (223 >= 8)
# (ans,m) = (1 + 1, 223 - 8) : 2
# (ans,m) = (2,215)
# while (215 >= 8).... while (7 >= 8) False
#return 28

#Question 3
def hs(n):
    f = 0
    for i in range (1, n + 1):
        if n % i == 0:
            f = f + 1
    #print(f %2 == 1)
    return (f %2 == 1)

hs(1)
hs(2)
hs(100)
hs(99)
hs(81)
hs(0)
# Only a perfect square

#Question 4
def f(m):
    if m == 0:
        return(0)
    else:
        print(m + f(m-1))
        return(m + f(m-1))    

# f(0)
# f(1)
# f(2)
# f(-1)

#SOLUTION:
# m = 0
# 0

# m = 1
# 1 + f(1 - 1)
# 1 + f(0)
# 1 + 0 
# 1

# m = 2
# 2 + f(2 - 1)
# 2 + f(1)
# 2 + 1 + f(1 - 1)
# 3 + 0
# 3 

# m = -1
# -1 + f(-1 -1)
# -1 + f(-2)
# -1 + -2 + f(-2 -1)
# ... infinite
# n(n-1)/2 form















    
    

