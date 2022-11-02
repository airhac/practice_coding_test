import sys
input = sys.stdin.readline

N = int(input())
h = list(map(int, input().split()))
         
tot = sum(h)   
dp = [[False] * (tot + 1) for _ in range(tot + 1)]
dp[0][0] = True

for k in range(N):
    for i in range( 2 * tot//3, -1, -1):
        for j in range(tot//3, -1, -1):
            if i - h[k] >= 0:
                dp[i][j] |= dp[i - h[k]][j]
            if j - h[k] >= 0:
                dp[i][j] |= dp[i][j - h[k]]

answer = 0
for i in range(tot + 1):
    for j in range(i + 1):
        if dp[i][j] and (j >= (tot - i - j)):
            answer = max(answer, tot - i - j)
print(answer)
                