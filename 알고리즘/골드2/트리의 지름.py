import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
graph = [[] for _ in range(t + 1)]
for _ in range(t):
    start, *nodes = list(map(int, input().split()))
    for i in range(0,len(nodes), 2):
        if nodes[i:i + 1][0] != -1:
            graph[start].append(nodes[i: i + 2])
def bfs(graph, start):
    distance = [0] * (t + 1)
    visited = [False] * (t + 1)
    q = deque([(start, 0)])
    visited[start] = True
    
    while q:
        now, dist = q.popleft()
        for i in graph[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                cost = dist + i[1]
                if distance[i[0]] < cost:
                    distance[i[0]] = cost
                    q.append((i[0], cost))
    return max(distance), distance.index(max(distance))

_, node = bfs(graph, 1)
answer, _ = bfs(graph, node)
print(answer)