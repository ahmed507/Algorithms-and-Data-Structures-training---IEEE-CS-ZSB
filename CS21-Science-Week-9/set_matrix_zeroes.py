def setZeroes(matrix):
    zeroes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                zeroes.append([i,j])
    print(zeroes)
    for x,y in zeroes:
        matrix[x][:]=[0]*len(matrix[:][0])
        for k in matrix:
            k[y] = 0
    print(matrix)

setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])

