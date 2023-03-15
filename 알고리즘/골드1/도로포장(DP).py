import sys
import heapq
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])
INF = sys.maxsize
dp = [[INF] * (k + 1) for _ in range(n + 1)] 
q = [[0, 1, 0]]
for i in range(k + 1):
    dp[1][i] = 0
heapq.heapify(q)
while q:
    dist, now, allow = heapq.heappop(q)
    if dp[now][allow] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]

        if dp[i[0]][allow] > cost:
            dp[i[0]][allow] = cost
            heapq.heappush(q, [cost, i[0], allow])
            
        if allow < k and dp[i[0]][allow + 1] > dist:
            dp[i[0]][allow + 1] = dist
            heapq.heappush(q, [dist, i[0], allow + 1])

print(min(dp[n]))
