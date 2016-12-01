

def MultiplyingMatrices(matrix1,matrix2,finalMatrix):
  for i in range(len(matrix1)): #iterating through the rows
    for j in range(len(matrix1)): #iterating through elements in each row
      for k in range(len(matrix1)): #iterating through the columns
        counter = matrix1[i][k] * matrix2[k][j] #product of the two number in matrix
        finalMatrix[i][j] = counter + finalMatrix[i][j] #adding the product to the value in the final matrix
        

  return(finalMatrix)

def MultiplyingMatrix(matrix1,B):

  for i in range(len(matrix1)): #iterating through the rows
    for j in range(len(matrix1)): #iterating through elements in each row
      matrix1[i][j] = matrix1[i][j]*B
      
     

  return(matrix1)

def AddingMatrices(matrix1,matrix2):

  for i in range (len(matrix1)): #iterating through the rows
    for j in range(len(matrix1)): #iterating through elements in each row
      matrix1[i][j] = matrix1[i][j] + matrix2[i][j]
      

  return(matrix1)

def SubtractingMatrices(matrix1,matrix2):

  for i in range (len(matrix1)): #iterating through the rows
    for j in range(len(matrix1)): #iterating through elements in each row
      matrix1[i][j] = matrix1[i][j] - matrix2[i][j]

  return(matrix1)


#Computing A = B*C - 2(B+C)

B = [[3,1],[2,4]]
C = [[2,10],[4,3]]
matrix = [[0,0],[0,0]]

x = MultiplyingMatrices(B,C,matrix)
y = AddingMatrices(B,C)
z = MultiplyingMatrix(y,2)

print("A = " + str(SubtractingMatrices(x,z)))





      



    
      

  



