
def BinarySearch(aList,lowI,upI):
    """Enter a sorted array and an lower and upper interval and this fucntion \n
    will return a boolean showing whether a element(s) in the array fit within that range"""
    
    
    lowestValue = 0
    highestValue = len(aList) - 1
    
    found = False

    #if len(aList) == 1 and aList[0] not in range(lowI,upI):
        #return(False)
    #elif len(aList) == 1 and aList[0] in range(lowI,upI):
        #return(True)
    
    while lowestValue <= highestValue and not found:
        
        middle = lowestValue + (highestValue//2)
        print("Current Middle >> " + str(middle))
        
        if aList[middle] in range(lowI,upI):

            found = True

        
        elif lowI > aList[middle]:
            lowestValue = middle + 1
            
        elif upI < aList[middle]:
            highestValue = middle - 1
            

    return(found)
                
                
print(BinarySearch([2,3,5,7,9,13],4,6))            
        
            
            
