import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(4)]
m = 0
n = 0
for x1, y1, x2, y2 in arr:
    m = max(m, x1, x2)
    n = max(n, y1, y2)
    
graph = [[0] * (m + 1) for _ in range(n + 1)]
for x1, y1, x2, y2 in arr:
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1
            
for g in graph:
    print(g)
    
answer = 0            
for i in range(n + 1):
    for j in range(m + 1):
        if graph[i][j] > 0:
            answer += 1
print(answer)