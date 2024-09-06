if __name__ == '__main__':
    mat = [[1,2,3,13],
              [4,5,6,14],
              [7,8,9,15],
              [10,11,12,16]]
              
    
    primary_diagonal = []
    secondary_diagonal = []
    n = len(mat)

    for i in range(n):
        primary_diagonal.append(mat[i][i])
    for i in range(n):
        if i != n - i - 1:
            secondary_diagonal.append(mat[i][n - i - 1])

    print(sum(primary_diagonal)+sum(secondary_diagonal))