import sys
input = sys.stdin.readline
n, h = map(int, input().split())
dp = [0] * (h + 1)
for i in range(n):
    ob = int(input())
    if i % 2 == 0:
        dp[0] += 1
        dp[ob] -= 1
    else:
        dp[h - ob] += 1
        dp[h] -= 1
for i in range(1, h):
    dp[i] = dp[i] + dp[i - 1]
print(min(dp[:-1]), dp.count(min(dp[:-1])))