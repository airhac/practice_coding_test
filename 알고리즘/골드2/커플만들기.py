import sys
n, m = map(int, input().split())
mans = list(map(int, input().split()))
womans = list(map(int, input().split()))

mans.sort()
womans.sort()

dp = [[0] * (m + 1) for _ in  range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j - 1] + abs(mans[i - 1] - womans[j - 1])
        if i > j:
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
        elif i < j:
            dp[i][j] = min(dp[i][j], dp[i][j - 1])
print(dp[n][m])