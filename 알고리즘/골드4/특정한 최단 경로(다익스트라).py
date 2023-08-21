import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    
u, v = map(int, input().split())
INF = int(1e10)

def dijkstra(start, end):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = [[0, start]]
    heapq.heapify(q)

    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:continue
        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    
    return distance[end]

main_path = dijkstra(u, v)
path1 = dijkstra(1, u) + main_path + dijkstra(v, n)
path2 = dijkstra(1, v) + main_path + dijkstra(u, n)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))