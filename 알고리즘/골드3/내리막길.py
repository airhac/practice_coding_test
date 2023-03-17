import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline
n, m  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
     # 탐색하지 않은 곳이라면 탐색
    if dp[x][y] == -1:
        dp[x][y] = 0 # 탐색 유무
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[x][y] > graph[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]
print(dfs(0, 0))

