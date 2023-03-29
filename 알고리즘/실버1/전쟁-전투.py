import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
def bfs(team, i, j):
    q = deque([[i, j]])
    res = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0<=nx<m and 0<=ny<n and visited[nx][ny] == 0 and graph[nx][ny] == team:
                visited[nx][ny] = 1
                q.append([nx, ny])
                res += 1
    return res ** 2

white_team = 0
blue_team = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            team = graph[i][j]
            visited[i][j] = 1
            if team == 'W':
                white_team += bfs(team, i, j)
            else:
                blue_team += bfs(team,i, j)
print(white_team, blue_team)