import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def BFS(start):
    visited = [0] * (n + 1)
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if not visited[i]:
                parents[i] = now
                q.append(i)
                visited[i] = 1
        
BFS(1)
for i in range(2, n + 1):
    print(parents[i])