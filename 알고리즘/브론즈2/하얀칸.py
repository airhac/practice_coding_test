import sys
input = sys.stdin.readline
graph = [list(input().rstrip()) for _ in range(8)]
answer = 0
print(len(graph))
print(len(graph[0]))
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                if graph[i][j] == 'F':
                    answer += 1
        else:
            if j % 2 != 0:
                if graph[i][j] == 'F':
                    answer += 1
print(answer)