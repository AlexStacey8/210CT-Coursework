#Task 2 basiz
def TrailingZeros(factorial):
    """ Given a number (factorial) this function will count the number of trailing zeros"""

    import math 

    #x is the number I will divide the factorial by, it will start at ten and the be multiplied by ten in each iteration
    #n is the number of trailing zeros. n has to start as negative one as it will run the while loop one more time adding an extra one before it know to terminate.
    #a is a variable that will cut off the while loop when it drops below 1, meaning that the factorial isn't devisable by the multiple of ten
    
    Fnumber = int(math.factorial(factorial))
    
    x = 10
    n = -1
    a = 0
    while a == 0:
        a = Fnumber%x #if the remainder is 0 than the factorial is a multiple of ten and has a trailing zero
        x = x*10
        n = n + 1

    return(n)
