def ExtractSubSquence(aList):

    """This Fuction takes a list of numbers and extracts the longest sub sequence \n
    of numbers that are in ascending order"""
    
    subSequence = []
    counter = 0
   
    for i in range(len(aList)):
        
        if i == len(aList)-1:
            return("The Longest Sub Sequence is >> " + str(longestSubSequence))
    
        elif aList[i] < aList[i+1]:
            subSequence.append(aList[i])
            

        elif aList[i] > aList[i+1]:
            subSequence.append(aList[i])

            
            if counter < len(subSequence):
                counter = len(subSequence)
                longestSubSequence = []
                for i in range(len(subSequence)):

                    longestSubSequence.append(subSequence[i])

                subSequence = []

                
    
    return(counter)
            
            
            
                
                            
print(ExtractSubSquence([1,2,1,5,8,9,3,4]))
