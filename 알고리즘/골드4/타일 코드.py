import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * 40
symmetric = [0] * 40
dp[1] = 1
dp[2] = 3
symmetric[1] = 1
symmetric[2] = 3
symmetric[3] = 1
symmetric[4] = 5
for i in range(3, n + 1):
    dp[i] = 2 * dp[i - 2] + dp[i - 1]
for i in range(5, n + 1):
    symmetric[i] = 2 * symmetric[i - 4] + symmetric[i - 2]
print((dp[n] - symmetric[n]) // 2 + symmetric[n]) 