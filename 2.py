#Matan Sofer 208491811
#Matan Ohayon 311435614


#function for matrix multiply (allowed only for matrix from same size) , return a matrix
def multiplyMatrix(matrix1,matrix2,rowsCol):
    result=[]
    for q in range(rowsCol):
        result.append ([])
        for m in range(rowsCol):                            ## creating new deafult matrix
            result[q].append(0)
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):                         ##multiply rowXcol
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


##This function is used for multiply matrix with 1D vector , return a vector
def MulMatrixVector(InversedMat, b_vector, rows):
    result = []
    for q in range(rows):
        result.append([])                                                    ## creating new deafult matrix
        result[q].append(0)
    for i in range(len(InversedMat)):
        for j in range(len(b_vector[0])):                                    ##mul inversed matrix with vector b
            for k in range(len(b_vector)):
                result[i][j] += InversedMat[i][k] * b_vector[k][j]
    return result
##This function calculate the matrix norma
def Norma(matrix1,rowsCol):
    max=0
    for i in matrix1:
        sum=0
        for j in i:   ##finding for each row the maximum val
            sum = sum+ abs(j)
        if sum > max :
            max = sum
    return max
##This function get a matrix and returns NEW matrix with same values
def copy_matrix(M,rowsCol):
    zerosMat=[]
    for q in range(rowsCol):
        zerosMat.append([])
        for m in range(rowsCol):                                 ## creating new deafult temporary matrix
            zerosMat[q].append(0)
    for i in range(rowsCol):
        for j in range(rowsCol):
            zerosMat[i][j] = M[i][j]                            ##copy the elements
    return zerosMat

##This function is calculate The inverse matrix by GeussianElimination method ,the function returns the inversed matrix
def GeussianElimination(matrix1,b_vector,rowsCol):
    elementaricMatrix = []   ##create new elementaric matrix
    for q in range(rowsCol):
        elementaricMatrix.append([])
        for m in range(rowsCol):
            elementaricMatrix[q].append(0)
        elementaricMatrix[q][q]=1

    allElementericSMultiply = copy_matrix(elementaricMatrix,rowsCol)
    for i in range(rowsCol):   ##finding for each column the max index val and if needed replace with row with the pivot row
      ElementaricM  = copy_matrix(elementaricMatrix,rowsCol)
      pivot = matrix1[i][i]
      count = 0
      linetoreplace=0
      max = pivot
      for j in range(1,rowsCol-i):
          count = count+1
          if abs(matrix1[i+j][i]) > max:
              max = abs(matrix1[i+j][i])
              linetoreplace = count
      if linetoreplace > 0 :
          ElementaricM[i][i]=0
          ElementaricM[i+linetoreplace][i+linetoreplace]=0
          ElementaricM[i+linetoreplace][i]=1
          ElementaricM[i][i+linetoreplace] = 1
          allElementericSMultiply = multiplyMatrix(ElementaricM, allElementericSMultiply, rowsCol)
          matrix1 = multiplyMatrix(ElementaricM, matrix1, rowsCol)
          ElementaricM = copy_matrix(elementaricMatrix, rowsCol)

      ElementaricM[i][i]=1/matrix1[i][i]
      allElementericSMultiply = multiplyMatrix(ElementaricM,allElementericSMultiply,rowsCol)
      matrix1 = multiplyMatrix(ElementaricM,matrix1,rowsCol)

      for j in range(i+1,rowsCol):   ##multiply by the matched elementeric to make all indexed under the pivot to zeros
          ElementaricM = copy_matrix(elementaricMatrix,rowsCol)
          ElementaricM[j][i]=-matrix1[j][i]
          allElementericSMultiply = multiplyMatrix(ElementaricM, allElementericSMultiply,rowsCol)
          matrix1 = multiplyMatrix(ElementaricM, matrix1, rowsCol)
    for i in range(rowsCol-1,0,-1):   ## above all pivots makes them zeros
      for j in range(i-1,-1,-1):
          ElementaricM = copy_matrix(elementaricMatrix,rowsCol)
          ElementaricM[j][i]=-matrix1[j][i]
          allElementericSMultiply = multiplyMatrix(ElementaricM, allElementericSMultiply,rowsCol)
          matrix1 = multiplyMatrix(ElementaricM, matrix1, rowsCol)

    return allElementericSMultiply  ##return the multiply of the elemnteric whith is that the inverse matrix


##This function is using LU method ,we are printing the l matrix , u matrix (and also the mul between them).
def LUpiruk(matrix1,b_vector,rowsCol):
    elementaricMatrix = []
    Lmatrix = []

    for q in range(rowsCol):
        elementaricMatrix.append([])
        Lmatrix.append([])                                      ## creating nelementric matrix
        for m in range(rowsCol):                                 ## and initializ them
            elementaricMatrix[q].append(0)
            Lmatrix[q].append(0)
        elementaricMatrix[q][q] = 1


    allElementericSMultiply = copy_matrix(elementaricMatrix, rowsCol)

    for i in range(rowsCol):   ##check if pivot zero , and if needed replace it with another row
        ElementaricM = copy_matrix(elementaricMatrix, rowsCol)
        if matrix1[i][i] == 0:
            for j in range(1, rowsCol - i):
                if matrix1[i + j][i] != 0:
                    ElementaricM[i][i] = 0
                    ElementaricM[i + j][i + j] = 0
                    ElementaricM[i + j][i] = 1
                    ElementaricM[i][i + j] = 1
                    allElementericSMultiply = multiplyMatrix(ElementaricM, allElementericSMultiply, rowsCol)
                    matrix1 = multiplyMatrix(ElementaricM, matrix1, rowsCol)
                    ElementaricM = copy_matrix(elementaricMatrix, rowsCol)
                    break
        for j in range(i+1, rowsCol):##multiply by the matched elementeric to make all indexed under the pivot to zeros
            ElementaricM = copy_matrix(elementaricMatrix,rowsCol)
            ElementaricM[j][i] = -matrix1[j][i]/matrix1[i][i]
            matrix1 = multiplyMatrix(ElementaricM, matrix1, rowsCol)
            allElementericSMultiply = multiplyMatrix(ElementaricM, allElementericSMultiply, rowsCol)

    allElementericSMultiply = GeussianElimination( allElementericSMultiply, b_vector,rowsCol)  ##inverse all elementaric multiply which is that L MATRIX
    Lmatrix = allElementericSMultiply
    Umatrix = matrix1  ##matrix1 is the u matrix
    print("U matrix  is :", Umatrix)                                                            ##printing
    print("L matrix is :", Lmatrix)
    print("The multiply of LU equal to : " , multiplyMatrix(Lmatrix, matrix1, rowsCol))   ##this allowed us to check LU multiplication and then we can know if we did it right (we should get original matrix)
#by the homework requirment

# mat1 = [[1,2,-2],[1,1,1],[2,2,1]]
# sizeOfmat1 =len(mat1)
# b_Vector1 =[[7],[2],[5])
#
# LUpiruk(mat1,b_Vector1,sizeOfmat1)
######################################################################

mat1 = [[1,2,-2],[1,1,1],[2,2,1]]
sizeOfmat1 =len(mat1)
b_Vector1 =[[7],[2],[5]]

InversedMat1=GeussianElimination(mat1,b_Vector1,sizeOfmat1)


# NormMatrix2 = Norma(mat2,sizeOfmat2)
# NormMatrix2Inverse = Norma(InversedMat2,sizeOfmat2)
# print("The cond of the matrix is : "  , NormMatrix2  * NormMatrix2Inverse )
print("final result for x=(A^-1) * b is : ",MulMatrixVector(InversedMat1, b_Vector1, sizeOfmat1))
