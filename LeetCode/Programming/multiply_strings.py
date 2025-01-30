matrix = [[1,1,1],[1,0,1],[1,1,1]]

zeros = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            col = matrix[i][j]
            row = i
            zeros.append((i,j))

for row, col in zeros:
    for j in range(len(matrix[row])):
        matrix[row][j] = 0

    for i in range(len(matrix)):
        matrix[i][col]=0


print(matrix)

