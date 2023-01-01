# #bit연산자로 위아래 만 비교 비교할때 3번만 비교하면 되니
# #최대 500 * 3 = 1500 정도의 소요시간이 걸리게됩니다.
# import sys
# input = sys.stdin.readline
# r, c = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(r)]
# arr = []
# for g in zip(*graph):
# 	g = ''.join(list(g))
# 	g = g.replace('.', '1')
# 	g = g.replace('x', '0')
# 	arr.append(g)
# # for a in arr:
# # 	print(a)
# answer = r + 1
# for i in range(c - 1):
#     print(arr[i])
#     print(bin(int(arr[i + 1], 2))[2:].zfill(r)[-r:])
#     tmp = bin(int(arr[i], 2) & int(arr[i + 1], 2))[2:].zfill(r).count('1')
#     tmp1 = bin(int(arr[i], 2) & int(bin(int(arr[i + 1], 2) << 1)[2:].zfill(r)[-r:], 2))[2:].zfill(r).count('1')
#     tmp2 = bin(int(arr[i], 2) & int(bin(int(arr[i + 1], 2) >> 1)[2:].zfill(r)[-r:], 2))[2:].zfill(r).count('1')
#     res = max(tmp, tmp1, tmp2)
#     print(res)
#     answer = min(answer, res)
# print(answer)
#이진으로 하면 위치가 달라지는 경우가 생긴다
#그리디 + dfs를 이용한 문제 각 라인마다 3번만 확인해주면 된다. 그리고 위에서 부터 확인해주면서 파이프를 연결할 수 있는지 확인 
import sys
input = sys.stdin.readline
r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
visited = [[True] * c  for _ in range(r)]
dx = [-1, 0, 1]
dy = [1, 1, 1]
def connect(x, y):
    if y == c - 1:
        return True
    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] and graph[nx][ny] == '.':
            visited[nx][ny] = False
            if connect(nx, ny):
                return True
    return False
answer = 0
for i in range(r):
    if graph[i][0] == '.':
        if connect(i, 0):
            answer += 1
print(answer)