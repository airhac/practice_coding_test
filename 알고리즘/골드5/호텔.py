import sys
input = sys.stdin.readline
c, n = map(int, input().split())
INF = int(1e9)
dp = [INF] * (c + 100)
cities = [list(map(int, input().split())) for _ in range(n)]
answer = INF
dp[0] = 0
for city in cities:
    loc = city[1]
    while True:
        dp[loc] = min(dp[loc - city[1]] + city[0], dp[loc])
        if loc >= c:
            answer = min(dp[loc], answer)
        if c + 100 == loc + 1:
            break
        loc += 1
print(answer)
#############
# import sys
# input = sys.stdin.readline
# c, n = map(int, input().split())
# INF = int(1e9)
# dp = [INF] * (1001)
# cities = [list(map(int, input().split())) for _ in range(n)]
# dp[0] = 0 
# for cost, people in cities:
#     for i in range(people, c + 100):
#         dp[i] = min(dp[i - people] + cost, dp[i])
        
# print(min(dp[c:]))