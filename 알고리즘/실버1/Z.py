import sys
input = sys.stdin.readline
n, x, y = map(int, input().split())
def dfs(n, x, y):
    if n == 0:
        return 0
    num = 2 * (x % 2) + (y % 2) + 4 * dfs(n - 1, x // 2, y // 2)
    return num
print(dfs(n, x, y))