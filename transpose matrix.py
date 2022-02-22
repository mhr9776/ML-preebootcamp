def transpose(matrice):
    if len(matrice) == len(matrice[0]):
        resul = [[0 for x in range(len(matrice[0]))]
                 for y in range(len(matrice))]
        for i in range(len(matrice)):
            for j in range(len(matrice[0])):
                resul[i][j] = matrice[j][i]
    elif len(matrice) != len(matrice[0]):
        resul = [[0 for x in range(len(matrice))]
                 for y in range(len(matrice[0]))]
        for i in range(len(matrice[0])):
            for j in range(len(matrice)):
                resul[i][j] = matrice[j][i]
    return resul


mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transpose(mat1))
