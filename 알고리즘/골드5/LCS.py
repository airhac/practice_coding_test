import sys
input = sys.stdin.readline

string_a = ' ' + input().rstrip()
string_b = ' ' + input().rstrip()
n = len(string_a)
m = len(string_b)
dp = [[0] * m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if string_a[i] == string_b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
print(dp[-1][-1])