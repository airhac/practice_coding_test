# import sys
# input = sys.stdin.readline
# N = int(input())
# answer = 0
# start = 0
# grid = [0] * N
# check = [False] * N
# def is_possible(row):
#     for i in range(row):
#         if grid[i] == grid[row] or abs(row - i) == abs(grid[row] - grid[i]):
#             return False
#     return True    
# def dfs(row):
#     global answer
    
#     if row == N :
#         answer += 1
#         return 
#     else:
#         for column in range(N):
#             if check[column]:
#                 continue
#             grid[row] = column
#             if is_possible(row):
#                 check[column] = True
#                 dfs(row + 1)
#                 check[column] = False
                
# dfs(start)
# print(answer)
#####
# import sys
# input = sys.stdin.readline
# N = int(input())
# answer = 0
# start = 0
# grid = [0] * N
# check = [False] * N
# def is_possible(row):
#     for i in range(row):
#         if grid[i] == grid[row] or abs(row - i) == abs(grid[row] - grid[i]):
#             return False
#     return True    
# def dfs(answer, row):
#     if row == N :
#         answer += 1
#         return answer
#     else:
#         for column in range(N):
#             if check[column]:
#                 continue
#             grid[row] = column
#             if is_possible(row):
#                 check[column] = True
#                 answer = dfs(answer, row + 1)
#                 check[column] = False
#     return answer
                
# print(dfs(answer, start))
import sys
input = sys.stdin.readline
N = int(input())
chess_board = [0] * N
check = [False] * N 
answer = 0

def is_possible(row):
    
    for i in range(row):
        if chess_board[i] == chess_board[row] or abs(chess_board[row] - chess_board[i]) == abs(row - i):
            return False
    return True
    
def dfs(answer, row):
    if row == N:
        answer += 1
        return answer
    for column in range(N):
        if check[column]:
            continue
        chess_board[row] = column
        if is_possible(row):
            check[column] = True
            answer = dfs(answer, row + 1)
            check[column] = False
    return answer
print(dfs(answer, 0))