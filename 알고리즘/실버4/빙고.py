import sys
from collections import defaultdict
input = sys.stdin.readline
graph = [list(map(int, input().split())) for _ in range(5)]
arr = []
loc = defaultdict(list)
for _ in range(5):
    arr += list(map(int, input().split()))
for i in range(5):
    for j in range(5):
        loc[graph[i][j]] = [i, j]
answer = 0
for index, num in enumerate(arr):
    x, y = loc[num]
    graph[x][y] = 0
    cnt = 0
    for g in graph:
        if sum(g) == 0:
            cnt += 1
    for g in zip(*graph):
        if sum(g) == 0:
            cnt += 1
    x = 0
    y = 0        
    for i in range(5):
        x += graph[i][i]
        y += graph[i][4 - i]
    if x == 0:
        cnt += 1
    if y == 0:
        cnt += 1
    if cnt >= 3:
        answer = index + 1
        break
print(answer)
####for문을 줄이고 인덱스 만으로도 가능