#Question 1
# n is positive 
# reversing digits

def intreverse(n):
    reverse = 0
    while n > 0:
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n =  n//10
        print(rev)
    return rev

#intreverse(783)
#  387
#intreverse(242789)
#  987242
#intreverse(3)
#  3

#SOLUTION:
# 783
# rev = 0
# 783 > 0
# reminder = 783 % 10 = 3
# reverse = 0 * 10 + 3 = 3
# 783 //10 = 78
# n = 78
# 78 > 0
# reminder = 78 % 10 = 8
# reverse = 3 * 10 + 8 = 38
# 78 //10 = 7
# n = 7
# 7 > 0
# remainder = 7 % 10 = 0
# reverse = 38 * 10 + 7 = 387
# 7 //10 = 0
# while False
# return 387

#Question 3
def sumprimes(number):
    sum = 0
    for i in range(2,len(number)):
        if (number[i] //2 ==0):
            sum = 0
        else:
            sum = sum + number[i]
            print(sum)
        print(sum)
        return(sum)
        
sumprimes([3,3,1,13])


