import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def mul(N, matrix1, matrix2):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += (matrix1[i][k] * matrix2[k][j])
            temp[i][j] %= 1000
    return temp

def devide(N, B, matrix):
    if B == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] % 1000
        return matrix
    
    tmp = devide(N, B // 2, matrix)
    if B % 2:
        return mul(N, mul(N, tmp, tmp), matrix)    
    else:
        return mul(N, tmp, tmp)
    
answer = devide(N, B, A)
for row in answer:
    print(*row)