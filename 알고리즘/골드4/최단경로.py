import heapq
import sys

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
INF = int(1e9)
distance = [INF] * (V + 1)

q = [[0, K]]
heapq.heapify(q)
distance[K] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = i[1] + dist
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, [cost, i[0]])
        
for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)