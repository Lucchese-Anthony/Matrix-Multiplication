import sys

def setMatrixSize(matrixSize):
    matrix = list()
    for i in range(matrixSize[0]):
        matrix.append([])
        for j in range(matrixSize[1]):
            matrix[i].append(0)
    return matrix
                    
def outputCurrentMatrix(matrixSize, matrix):
    for i in range(matrixSize[0]):
        print("| ", end="")
        for j in range(matrixSize[1]):
            print(f" {matrix[i][j]} ", end='')
        print(" |", end="\n")

def multiplyMatrices(matrix1, matrix2):
    if (len(matrix1[0]) != len(matrix2)):
        print("cannot multiply inconsistent-sized matrices")
        exit(0)
    newMatrixSize = [len(matrix1), len(matrix2[0])]
    newMatrix = setMatrixSize(newMatrixSize)
    for i in range(newMatrixSize[0]):
        for j in range(newMatrixSize[1]):
            for k in range(newMatrixSize[0]):
                val = 0
                for l in range(newMatrixSize[1]):
                    newMatrix[i][j] += matrix1[k][l] * matrix2[]

    return newMatrix

def main():
    matrix1size = str(input(f"How large is matrix 1 (nxm)> ")).split("x")
    for i in range(len(matrix1size)):
        matrix1size[i] = int(matrix1size[i])
    matrix2size = str(input(f"How large is matrix 2 (nxm)> ")).split("x")
    for i in range(len(matrix2size)):
        matrix2size[i] = int(matrix2size[i])
    matrix1 = setMatrixSize(matrix1size)
    matrix2 = setMatrixSize(matrix2size)
    for i in range(matrix1size[0]):
        for j in range(matrix1size[1]):
            insertVal = int(input(f"Matrix 1 | ({i+1}, {j+1}): "))
            print(insertVal)
            matrix1[i][j] = insertVal
            outputCurrentMatrix(matrix1size, matrix1)
    for i in range(matrix2size[0]):
        for j in range(matrix2size[1]):
            insertVal = int(input(f"Matrix 2 | ({i+1}, {j+1}): "))
            matrix2[i][j] = insertVal
            outputCurrentMatrix(matrix2size, matrix2)
    matrix3 = multiplyMatrices(matrix1, matrix2)

    outputCurrentMatrix([len(matrix3), len(matrix3[0])], matrix3)

if __name__ == "__main__":
    main()