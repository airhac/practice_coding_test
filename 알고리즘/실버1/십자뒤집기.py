import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
answer = []
def convert_bin(board):
    bin = ''
    for i in range(3):
        for j in range(3):
            bin += '0' if board[i][j] == '.' else '1'
    return int(bin, 2)
def convert_board(ret, x, y):
    dx, dy = [0, -1, 0, 1, 0], [0, 0, -1, 0, 1]
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            ret[nx][ny] = '*' if ret[nx][ny] == '.' else '.'
    return ret

def bfs(graph):
    init_board = [['.'] * 3 for _ in range(3)]
    visited = [0] * 1000
    
    q = deque([init_board])
    visited[convert_bin(init_board)] = 1
    time = 0
    while q:
        case = len(q)
        for _ in range(case):
            board = q.popleft()
            if board == graph:
                return time
            
            for i in range(3):
                for j in range(3):
                    arr = [b[:] for b in board]
                    next_board = convert_board(arr, i, j)
                    bin_num = convert_bin(next_board)
                    
                    if not visited[bin_num]:
                        q.append(next_board)
                        visited[bin_num] = 1
        time += 1
def solution(t):       
    for _ in range(t):
        graph = [list(input().strip()) for _ in range(3)]
        answer = bfs(graph)
        print(answer)
solution(t)