
def HighestPerfectSquare(x):
    """Given a positive integer this function will return the highest perfect square that is either equal or less than the number"""

    n = 1 #number to test 
    perfectSquare = 1 #current highest perfect square
        
    while n**2 <= x :
        perfectSquare = n**2
        n = n+1
        
        
    return("The Highest perfect suqare is >> " + str(perfectSquare))

        

        
