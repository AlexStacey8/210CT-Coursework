
def PrimeNumber(n,x):
  """n is the number you want to test and x = n-1"""
  
  if n <= 1:
    return("Your Number isn't Prime")
  elif n = 2:
    return("Your number is Prime")
  elif x = 1:
    return("Your number is Prime")
  elif n%x = 0:
    return("Your Number isn't Prime")
  elif n%x != 0:
    return(PrimeNumber(n,x-1))
  


print(PrimeNumber(17,16))
print(PrimeNumber(4,3))
print(PrimeNumber(1,0))


  
    
    
 
