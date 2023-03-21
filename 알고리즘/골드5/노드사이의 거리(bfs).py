import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visited = [0] * (n + 1)

def bfs(start, end):
    q = deque([[0, start]])
    visited[start] = 1
    
    while q:
        dist, now = q.popleft()
        if now == end:
            return dist
        for i in graph[now]:
            cost = dist + i[1]
            if visited[i[0]] != 1:
                visited[i[0]] = 1
                q.append([cost, i[0]])
    
for _ in range(m):
    visited = [0] * (n + 1)
    start, end = map(int, input().split())
    print(bfs(start, end))
