import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
c, r = map(int, input().split())
k = int(input())
graph = [[0] * r for _ in range(c)]
graph[0][0] = 1
d = 0
q = deque([[1, 0, 0]])
if c * r < k:
    print(0)
    exit()
while q:
    num, x, y = q.popleft()
    if num == k:
        break
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < c and 0 <= ny < r and graph[nx][ny] == 0:
        graph[nx][ny] = 1
        q.append([num + 1, nx, ny])
    else:
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]
        graph[nx][ny] = 1
        q.append([num + 1, nx, ny])
print(x + 1, y + 1)