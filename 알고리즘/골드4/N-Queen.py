import sys
input = sys.stdin.readline
N = int(input())
answer = 0
start = 0
grid = [0] * N

def is_possible(row):
    for i in range(row):
        if grid[i] == grid[row] or abs(row - i) == abs(grid[row] - grid[i]):
            return False
    return True    
def dfs(answer, row, N):
    if row == N :
        answer += 1
        return answer
    
    for column in range(4):
        grid[row] = column
        if is_possible(row):
            answer = dfs(answer, row + 1, N)

    return answer
print(dfs(answer, start, N))