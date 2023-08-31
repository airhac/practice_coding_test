import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
start, end = map(int, input().split())
INF = int(1e9)

def dijkstra(start, end):
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)
    
    q = [(0, start, [start])]
    heapq.heapify(q)
    
    visited[start] = True
    distance[start] = 0

    while q:
        dist, now, cities = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        if now == end:
            return dist, cities
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                cities.append(i[0])
                tmp = cities[::]
                heapq.heappush(q, (cost, i[0], tmp))
                cities.pop()
                
answer = dijkstra(start, end)
print(answer[0])
print(len(answer[1]))
for a in answer[1]:
    print(a, end=' ')