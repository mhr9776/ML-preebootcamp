from functools import reduce


def mat_mul_map(a, b):
    if len(a) == len(b[0]):
        resul = [[0 for x in range(len(b[0]))] for y in range(len(a))]
    for i in range(len(a)):
            for j in range(len(b[0])):
                resul[i][j] = reduce(lambda a, b: a + b, map(lambda x, y: x * y, a[i], [b[l][j] for l in range(len(a[0]))]))
    return resul


M = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
N = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]


print(mat_mul_map(M, N))
