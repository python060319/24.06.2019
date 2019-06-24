
arr1 = [6, 9, 20, 33]
resBool = []


matrix = [[6, 9, 20, 33], [1], [5, 7, 10, 20], [4, 8, 10]]
matrixBoolean = []

for lmatrix in matrix:
    subMatrix = []
    for number in lmatrix:
        subMatrix.append(number % 2 == 0)
    matrixBoolean.append(subMatrix)

print(matrixBoolean)







