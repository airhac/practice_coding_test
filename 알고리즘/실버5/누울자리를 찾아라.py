import sys
input = sys.stdin.readline
n = int(input())
graph = [input().rstrip() for _ in range(n)]
answer = 0
for g in graph:
    g = g.split('X')
    for l in g:
        if len(l) >= 2:
            answer += 1
print(answer, end=' ')
answer = 0
for g in zip(*graph):
    g = ''.join(g).split('X')
    for l in g:
        if len(l) >= 2:
            answer += 1
print(answer, end=' ')