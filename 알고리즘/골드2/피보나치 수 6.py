import sys
input = sys.stdin.readline

N = int(input())
A = [[1, 1], [1, 0]]

def mul(N, matrix1, matrix2):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (matrix1[i][k] * matrix2[k][j])
            temp[i][j] %= 1000000007
    return temp

def devide(N, matrix):
    if N == 1:
        for i in range(2):
            for j in range(2):
                matrix[i][j] %= 1000000007
        return matrix
    
    tmp = devide(N // 2, matrix)
    if N % 2:
        return mul(N, mul(N, tmp, tmp), matrix)    
    else:
        return mul(N, tmp, tmp)
    
print(devide(N, A)[0][1])
