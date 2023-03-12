import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
answer = 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
def dfs(answer, x, y, cnt):
    
    answer = max(answer, cnt)
    num = int(board[x][y])
    
    for i in range(4):
        nx, ny = x + num * dx[i], y + num * dy[i]
        
        if 0<=nx<n and 0<=ny<m and board[nx][ny] !='H' and cnt + 1 > dp[nx][ny]:
            if visited[nx][ny] != 0:
                return -1
            dp[nx][ny] = cnt + 1
            visited[nx][ny] = 1
            answer = dfs(answer, nx, ny, cnt + 1)
            visited[nx][ny] = 0
            if answer == -1:
                return -1
    return answer
answer = dfs(answer, 0, 0, 0)
if answer != -1:
    print(dfs(answer, 0, 0, 0) + 1)
else:
    print(-1)