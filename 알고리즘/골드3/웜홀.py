import sys

def bf(start):
    INF = int(1e9)
    distance = [INF] * (N + 1)
    distance[start] = 0
    
    for i in range(N):
        for edge in edges:
            s = edge[0]
            e = edge[1]
            dist = edge[2]
            
            if distance[e] > dist + distance[s]:
                distance[e] = dist + distance[s]
                if i == N - 1:
                    return True
    return False
for _ in range(int(input())):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
        edges.append([v, u, w])
        
    for _ in range(W):
        u, v, w = map(int, input().split())
        edges.append([u, v, -w])
    
    if bf(1):
        print('YES')
    else:
        print('NO')