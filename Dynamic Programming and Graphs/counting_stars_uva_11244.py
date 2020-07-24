move = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

if __name__ == "__main__":

    while True:
        n_row, n_column = map(int, input().split())
        matrix = []
        
        if n_row == 0 or n_column == 0:
            break

        for i in range(n_row):
            matrix.append(*input().split())
        
        count = 0
        print(matrix)

        for i in range(n_row):
            for j in range(n_column):
                if matrix[i][j] == '*':
                    star = True
                    for k in range(8):
                        a = i + move[k][0]
                        b = j + move[k][1]
                        if a >= 0 and a < n_row and b >= 0 and b < n_column and matrix[a][b] != '.':
                            star = False
                    if star:
                        count += 1
        print(count)



        
