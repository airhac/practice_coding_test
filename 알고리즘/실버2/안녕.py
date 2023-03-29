import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
sta = [0] + list(map(int, input().split()))
ple = [0] + list(map(int, input().split()))
#안에 내용은 기쁨, x축은 체력, y축은 사람 수 
dp = [[0] * 101 for _ in range(n + 1)]
for i in range(1, n + 1):
    #j는 체력 현재 가지고 있는 체력?
    for j in range(1, 101):
        if sta[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - sta[i]] + ple[i])
        else:
            dp[i][j] = dp[i - 1][j]
    
print(dp[n][99])