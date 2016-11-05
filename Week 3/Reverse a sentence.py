#Week 3 task 1    
def ReverseAString(sentence):
    listOfWords = sentence.split(" ")
    n = len(listOfWords) - 1
    reversedList = []
    for i in range(len(listOfWords)):
        word = listOfWords[n]
        reversedList.append(word)
        n = n - 1

    return(" ".join(reversedList))

    
print(ReverseAString("This Is Awesome"))   
    
#BigO O(n)    

    
    

    
    
    
