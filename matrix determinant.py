def new_matrix(matrice,i):
    if len(matrice) == 2 and len(matrice[0]):
        return matrice 

    else:
        temp = matrice[:]
        temp.pop(0)
        for j in temp:
            j.pop(i)

def determinant(matrice):
    if len(matrice) == 2:
        temp = matrice[0][0]*matrice[1][1] - matrice[1][0]*matrice[0][1]
        return temp
        
    else:
        temp = 0
        for i in range(len(matrice[0])):
            pro += ((-1)**i)*matrice[0][i]*determinant(new_matrix(matrice,i))    
        return temp  