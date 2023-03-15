import sys
input = sys.stdin.readline
n = int(input())
MAX = 1000
dp = [[[0] * 3 for _ in range(2)] for _ in range(MAX + 1)]
dp[1][0][0], dp[1][0][1], dp[1][1][0] = 1, 1, 1
for n in range(1, MAX):
    dp[n + 1][0][0] = (dp[n][0][0] + dp[n][0][1] + dp[n][0][2]) % 1000000
    dp[n + 1][0][1] = dp[n][0][0]
    dp[n + 1][0][2] = dp[n][0][1]
    dp[n + 1][1][0] = (dp[n][1][0] + dp[n][1][1] + dp[n][1][2] +
                       dp[n][0][0] + dp[n][0][1] + dp[n][0][2]) % 1000000
    dp[n + 1][1][1] = dp[n][1][0]
    dp[n + 1][1][2] = dp[n][1][1]
    
print((dp[n][1][0] + dp[n][1][1] + dp[n][1][2] + dp[n][0][0] + dp[n][0][1] + dp[n][0][2])%1000000)
