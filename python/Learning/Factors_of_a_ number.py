def factors(limit):
    # Define empty factor list
    flist = []
    # Running For loop from 1 to limit + 1
    for i in range(1, limit + 1):
        # If checks condition if the remainder is 0
        if limit % i == 0:
            # If so, then the number i is inputed in the list for each True iteration
            flist = flist + [i]
    print(flist)
    return(flist)

factors(101)