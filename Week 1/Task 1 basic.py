#Week 1 Tasks
#Task 1

def randomRearrange(yourList): 

    """This fuction will randomly shuffle the elements in a list"""
    
    import random


    for i in yourList:
        oldPos = yourList.index(i) #get the original position of the element in the list
        newPos = random.randint(0,(len(yourList)-1)) #get the new random position that the element will be moved to
        
        yourList[oldPos], yourList[newPos] = yourList[newPos], yourList[oldPos] #sawping the elements position 

    return(yourList)
    


#getting the user input through a loop so they can enter each element in there list individually 

listRange = int(input("How many elemnts are in your list? >> ")) 

listOfInts = []

for i in range(0,listRange):
    x = int(input("Enter element >> "))
    listOfInts.append(x)

print(randomRearrange(listOfInts)) 







    


