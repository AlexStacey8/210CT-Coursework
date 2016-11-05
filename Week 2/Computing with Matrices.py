

def MultiplyingMatrices(matrix1,matrix2,finalMatrix):
  for i in range(len(matrix1)):
    for j in range(len(matrix1)):
      for k in range(len(matrix1)):
        counter = matrix1[i][k] * matrix2[k][j]
        finalMatrix[i][j] = counter + finalMatrix[i][j]
        

  return(finalMatrix)

def MultiplyingMatrix(matrix1,B):

  for i in range(len(matrix1)):
    for j in range(len(matrix1)):
      matrix1[i][j] = matrix1[i][j]*B
      
     

  return(matrix1)

def AddingMatrices(matrix1,matrix2):

  for i in range (len(matrix1)):
    for j in range(len(matrix1)):
      matrix1[i][j] = matrix1[i][j] + matrix2[i][j]
      

  return(matrix1)

def SubtractingMatrices(matrix1,matrix2):

  for i in range (len(matrix1)):
    for j in range(len(matrix1)):
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





      



    
      

  



