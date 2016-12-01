def ExtractSubSquence(aList):

    """This Function takes a list of numbers and extracts the longest sub sequence \n
    of numbers that are in ascending order"""
    
    subSequence = []
    counter = 0 #keeps track of the length of the sub sequences to find the longest
   
    for i in range(len(aList)):
        
        if i == len(aList)-1:
            return("The Longest Sub Sequence is >> " + str(longestSubSequence))
    
        elif aList[i] < aList[i+1]:
            subSequence.append(aList[i])
            

        elif aList[i] > aList[i+1]:
            subSequence.append(aList[i])

            
            if counter < len(subSequence):
                counter = len(subSequence) #making the counter the length of the sub sequence 
                longestSubSequence = []
                
                for i in range(len(subSequence)):

                    longestSubSequence.append(subSequence[i]) # appending the element in the sub sequence to the longest sub sequence list

                subSequence = [] # restarting the sub sequence
                

                
    
    return(longestSubSequence)
            
            
            
                
list1 = [1,2,3,1,5,8,9,3,4,5,6,7,1]
list2 = [1,2,3,4,5,6,7,8,3,5,6,1,2]
list3 = [1,2,3,2,5,8,97,1,2,2]


print(ExtractSubSquence(list1))
print(ExtractSubSquence(list2))
print(ExtractSubSquence(list3))

