import sys
input = sys.stdin.readline
from collections import deque
def bfs(x, y):
        graph[x][y] = 0
        q = deque([[x, y]])
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append([nx, ny])
                    
        return 
    
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
        
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                bfs(i, j)
                answer += 1
    print(answer)