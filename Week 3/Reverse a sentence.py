#Week 3 task 1    
def ReverseAString(sentence):
    listOfWords = sentence.split(" ") #splitting sentence at spaces
    n = len(listOfWords) - 1 #index of last element in list
    reversedList = []
    for i in range(len(listOfWords)):
        #appending the words in the sentence in reverse order
        word = listOfWords[n] 
        reversedList.append(word)
        n = n - 1

    return(" ".join(reversedList))

    
print(ReverseAString("This Is Awesome"))   
    
#BigO O(n)    

    
    

    
    
    
