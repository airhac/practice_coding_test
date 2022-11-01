import sys
input = sys.stdin.readline
w, h  = map(int, input().split())
graph = [[[0]  * 4 for _ in range(w + 1)]  for _ in range(h + 1)]

for i in range(2, h + 1):
    graph[i][1][2] = 1
    
for i in range(2, w + 1):
    graph[1][i][0] = 1
    
for i in range(2, h + 1):
    for j in range(2, w + 1):
        graph[i][j][0] = graph[i][j - 1][0] + graph[i][j - 1][1]
        graph[i][j][1] = graph[i][j - 1][2]#현재 위치에서 동쪽으로 향하며, 회전하지 못하는 경우는 전 위치에서 남쪽으로 회전한 경우이다
        graph[i][j][2] = graph[i - 1][j][2]  + graph[i - 1][j][3]
        graph[i][j][3] = graph[i - 1][j][0]#현재 위치에서 남쪽으로 향하며, 회전하지 못하는 경우는 전 위치에서 동쪽으로 회전한 경우이다.

print(sum(graph[h][w]) % 100000)