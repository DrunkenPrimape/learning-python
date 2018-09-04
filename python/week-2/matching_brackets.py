def matched(string):
    # Initialize the number of brackets to 0, ie, all brackets are matched
    number_of_brackets = 0
    
    for character in string:
        if character == "(":
            # If a bracket is opened, increment the number of brackets
            number_of_brackets += 1
        elif character == ")":
            # If a bracket is closed, decrement the number of brackets
            number_of_brackets -= 1

        # At any point, if we have closed more brackets than we have opened
        # it is a mismatch and so break
        if(number_of_brackets < 0):
            break

    # the the number of brackets are 0 return true
    return number_of_brackets == 0
        

matched("zb%78")
#True

matched("(7)(a")
#False

matched("a)*(?")
#False
 
matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
#True