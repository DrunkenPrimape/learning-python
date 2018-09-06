def intreverse(n):
    reverse = 0
    while(n > 0):
        reminder = n % 10
        reverse = (reverse * 10) + reminder
        n = n//10
    print("%s" % reverse)
    return(reverse)

intreverse(783)
#  387
intreverse(242789)
#  987242
intreverse(3)