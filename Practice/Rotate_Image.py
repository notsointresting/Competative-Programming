#Rotate Image
N = int(input('Enter Number of rows---> '))
matrix = [ list(map(int,input().split())) for i in range(N)]
print(matrix)

# We will Transpose this matrix diagonally
for i in range(N):
    for j in range(i+1,N):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

# We will reverse each row of the matrix
for i in range(N):
    matrix[i] = matrix[i][::-1]

print(matrix)
