
def RemoveVowels(string):
    """ enter a string in lower case and this fuction will remove the vowels"""

    if 'a' in string:
        newString = string.replace('a','')
        
        return(RemoveVowels(newString))

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


