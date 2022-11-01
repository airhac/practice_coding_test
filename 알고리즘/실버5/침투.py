import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(M)]
answer = 'NO'
def solution(graph, M , N, answer):
    def bfs(graph, i, j):
        dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
        q = deque([(i, j)])
        graph[i][j] = 2
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))
        return graph
    for j in range(N):
        if graph[0][j] == 0:
            graph = bfs(graph, 0, j)
    
    for j in range(N):
        if graph[-1][j] == 2:
            answer = 'YES'
            break
    return answer
print(solution(graph, M, N, answer))