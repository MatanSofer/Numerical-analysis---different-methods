#Matan Sofer 208491811
#Matan Ohayon 311435614


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

##This function get a vector and returns NEW matrix with same values
def copy_vector(V,rowsCol):
    zerosVec=[]
    for q in range(rowsCol):
        zerosVec.append([])
    for m in range(rowsCol):                                 ## creating new deafult temporary vector
        zerosVec[m].append(0)
    for i in range(rowsCol):
        zerosVec[i][0] = V[i][0]                            ##copy the elements
    return zerosVec
##This function is for pivoting first column as requested
def Pivoting(matrix1,b_vector,rowsCol):

    newMat = copy_matrix(matrix1, rowsCol)
    newVec = copy_vector(b_vector,rowsCol)
    print(newMat)
    print(newVec)
    for i in range(1):
        pivot = matrix1[i][i]
        count = 0
        linetoreplace = 0
        max = pivot
        for j in range(1, rowsCol - i):
            count = count + 1
            if abs(matrix1[i + j][i]) > max:
                max = abs(matrix1[i + j][i])
                linetoreplace = count
        if linetoreplace > 0:
            newMat[i] = matrix1[linetoreplace+i]
            newMat[linetoreplace+i] = matrix1[i]
            newVec[i] = b_vector[linetoreplace+i]
            newVec[linetoreplace + i] = b_vector[i]

            matrix1[i] = newMat[i]
            matrix1[linetoreplace] = newMat[linetoreplace]
            b_vector[i] = newVec[i]
            b_vector[linetoreplace] = newVec[linetoreplace]

    return newMat
#check if matrix has "string diagonal and returns boolean value
def maxDiag(mat1 ,rowsCol):
    for i in range(len(mat1)):
        SumAllElements = 0
        for j in range(len(mat1)):
            SumAllElements = SumAllElements + abs(mat1[i][j])
        if abs(mat1[i][i]) < SumAllElements - abs((mat1[i][i])):
            return False
    return True

#yaakobi method for iteration solving method
def Yaakobi(mat1,b_Vector,rowsCol):
    x=0
    y=0
    z=0
    iterationNum=1
    afterPivot = Pivoting(mat1,b_Vector,rowsCol)
    if maxDiag(afterPivot, rowsCol):
        print("The matrix got DOMINATE DIAG : ")
    else:
        print("The matrix DONT HAVE DOMINATE DIAG : ")
    while(True):
        x1 = (b_Vector[0][0] - afterPivot[0][1] * y - afterPivot[0][2] * z) / afterPivot[0][0]
        y1 = (b_Vector[1][0] - afterPivot[1][0] * x - afterPivot[1][2] * z) / afterPivot[1][1]
        z1 = (b_Vector[2][0] - afterPivot[2][0] * x - afterPivot[2][1] * y) / afterPivot[2][2]
        if(abs(x1-x) < 0.00001 ) :
            break
        else:
            x = x1
            y = y1
            z = z1
        print(f"iteration Number {iterationNum} result are : x={x},y={y},z={z}")
        iterationNum=iterationNum+1

##guess ziedel method for iteration solving method
def GaussSeidel(mat1,b_Vector,rowsCol):
    x=0
    y=0
    z=0
    iterationNum=1
    afterPivot = Pivoting(mat1, b_Vector, rowsCol)
    if maxDiag(afterPivot, rowsCol):
        print("The matrix got DOMINATE DIAG : ")
    else:
        print("The matrix DONT HAVE DOMINATE DIAG : ")
    while(True):
        x1 = (b_Vector[0][0] - afterPivot[0][1] * y - afterPivot[0][2] * z) / afterPivot[0][0]
        y1 = (b_Vector[1][0] - afterPivot[1][0] * x1 - afterPivot[1][2] * z) / afterPivot[1][1]
        z1 = (b_Vector[2][0] - afterPivot[2][0] * x1 - afterPivot[2][1] * y1) / afterPivot[2][2]
        if((abs(x1-x) < 0.00001 ) ) :
            break
        else:
            x = x1
            y = y1
            z = z1
        print(f"iteration Number {iterationNum} result are : x={x},y={y},z={z}")
        iterationNum=iterationNum+1



#set a matrix and vector
mat1=[[4,2,0] ,[2,10,4], [0,4,5]]
b_Vector=[[2],[6],[5]]
rowsCol =len(mat1)

##asking from user for which method he want  , and return the value
x = int(input('choose 1 for  Yaakobi metho1d\nchoose 2 for Gauss–Seidel\n'))

if x == 1:
    print("-----Yaakobi metho1d-----")
    Yaakobi(mat1,b_Vector, rowsCol)
else:
    print("-----Gauss–Seidel method-----")
    GaussSeidel(mat1,b_Vector, rowsCol)








