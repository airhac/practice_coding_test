import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def bfs(start):
    result = [items[start]]
    visited = [False] * (n + 1)
    q = deque([(start, 0)])
    visited[start] = True
    
    while q:
        now, dist = q.popleft()
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost <= m:
                result.append(items[i[0]])
                visited[i[0]] = True
                q.append((i[0], cost))
    return result

answer = 0
for i in range(1, n + 1):
    answer = max(answer, sum(bfs(i)))
print(answer)