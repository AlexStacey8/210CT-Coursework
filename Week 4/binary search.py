
def BinarySearch(aList,lowI,upI):
    """Enter a sorted array and a lower and upper interval and this fucntion \n
    will return a Boolean showing whether an element(s) in the array fit within that range"""
    
    lowestValue = 0
    highestValue = len(aList) - 1
    
    found = False
    
    while lowestValue <= highestValue and not found:
        
        middle = lowestValue + (highestValue//2) #gets the middle value
        print("Current Middle >> " + str(middle))
        
        if aList[middle] in range(lowI,upI): #if the middle value is within the range then return true

            found = True

        
        elif lowI > aList[middle]:
            #if lower interval is greater than the middle value
            #make the lowest value the middle + 1 
            lowestValue = middle + 1 
            
        elif upI < aList[middle]:
            #if uper interval is less than the middle
            #make the middle value the middle - 1
            highestValue = middle - 1
            

    return(found)
                
                
print(BinarySearch([2,3,5,7,9,13],4,6))            
        
            
            
