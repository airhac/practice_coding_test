import sys
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
b_map = [[0] * N for _ in range(N)]
K = M // 2
for i in range(K, N - K):
    for j in range(K, N - K):
        b_map[i][j] = map[i - K][j - K]
        if i - K - 1 >= 0:
            b_map[i][j] -= map[i - K - 1][j - K]
        if j - K - 1 >= 0:
            b_map[i][j] -= map[i - K][j - K - 1]
        if i - K - 1 >= 0 and j - K - 1 >= 0:
            b_map[i][j] += map[i - K - 1][j - K - 1]
        if i - M >= 0:
            b_map[i][j] += b_map[i - M][j]
        if j - M >= 0:
            b_map[i][j] += b_map[i][j - M]
        if i - M >= 0 and j - M >= 0:
            b_map[i][j] -= b_map[i - M][j - M]
         
for m in b_map:
    for n in m:
        print(-n, end=' ')
    print()
    