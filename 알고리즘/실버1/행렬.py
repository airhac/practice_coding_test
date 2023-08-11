import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr_A = [list(map(int, list(input().rstrip()))) for _ in range(h)]
arr_B = [list(map(int, list(input().rstrip()))) for _ in range(h)]

def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            arr_A[i][j] = 1 - arr_A[i][j]

def check():
    for i in range(h):
        for j in range(w):
            if arr_A[i][j] != arr_B[i][j]:
                return False
    return True

answer = 0

for i in range(h - 2):
    for j in range(w - 2):
        if arr_A[i][j] != arr_B[i][j]:
            reverse(i, j)
            answer += 1

if check():
    print(answer)
else:
    print(-1)