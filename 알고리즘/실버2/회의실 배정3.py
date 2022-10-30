import sys
input = sys.stdin.readline
N = int(input())
onboards = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)
for i in range(N):
    dp[i + 1] = onboards[i][-1] 
for i in range(2, N + 1):
    dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
print(dp[N])
