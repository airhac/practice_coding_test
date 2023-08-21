import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
#추가로 무언가 여부를 확인하여 방문기록을 남길때는 3차원으로 여부를 확인
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def BFS():
    q = deque([])
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    
    while q:
        x, y, check = q.popleft()
            
        if x == n - 1 and y == m - 1:
            return visited[x][y][check]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m  and visited[nx][ny][check] == 0:
                if graph[nx][ny] == 0:
                    q.append((nx, ny, check))
                    visited[nx][ny][check] = visited[x][y][check] + 1
                
                if check == 0 and graph[nx][ny] == 1:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][check] + 1
    return -1

print(BFS())
# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
# dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
# # 이전에 벽을 뚫지 않았을때의 visited와 이전에 벽을 뚫었을 경우 visited를 나누어 보아야한다.
# def BFS(graph, x, y):
#     q = deque([])
    
#     visited = [[0] * m for _ in range(n)]
#     visited[x][y] = 1
#     q.append([x, y, 1, False])
#     while q:
#         x, y, dist, check = q.popleft()
            
#         if x == n - 1 and y == m - 1:
#             return dist
        
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m  and visited[nx][ny] == 0:
#                 if graph[nx][ny] == 1:
#                     if not check:
#                         q.append([nx, ny, dist + 1, True])
#                         visited[nx][ny] = 1
#                 else:
#                     q.append([nx, ny, dist + 1, check])
#                     visited[nx][ny] = 1
                    
#     return -1

# print(BFS(graph, 0, 0))