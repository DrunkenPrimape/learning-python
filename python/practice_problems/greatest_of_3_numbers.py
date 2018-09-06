def greatest(l,m,n):
    
    if m >= n:
        if l >= m:
            print("%s" %l)
            return l
        
        else:
            print("%s" %m)
            return m
    
    else:
        if l>= n:
            print("%s" %l)
            return l

        else:
            print("%s" %n)
            return n


greatest(1,2,3)
# 3
greatest(2,2,1)
# 2
greatest(4,3,2)
#4
greatest(5,5,5)
#5
greatest(0,0,1)
#1
greatest(0,2,0)
#2
greatest(-1,-2,-3)
#-1
greatest(-2,-2,-4)
#-2
greatest(0,-2,0)
#0
    
    
