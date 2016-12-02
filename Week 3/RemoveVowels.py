
def RemoveVowels(string):
    """ enter a string in lower case and this function will remove the vowels"""
    
    if 'a' in string:
        newString = string.replace('a','') #removes the vowel from the string
        
        return(RemoveVowels(newString)) #calls function again until the sting has no more vowels

    elif 'e' in string:
        newString =  string.replace('e','')
        
        return(RemoveVowels(newString))

    elif 'i' in string:
        newString =  string.replace('i','')
        
        return(RemoveVowels(newString))
        

    elif 'o' in string:
        newString =  string.replace('o','')
        
        return(RemoveVowels(newString))

    elif 'u'in string:
        newString =  string.replace('u','')
        
        return(RemoveVowels(newString))

    else:
        return('Your word without vowels >> ' + str(string))


print(RemoveVowels('beautiful'))
