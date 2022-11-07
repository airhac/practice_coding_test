import sys
input = sys.stdin.readline
w, h = map(int, input().split())
y, x = map(int, input().split())
d = 0
dx, dy = [1, 1, -1, -1], [1, -1, -1, 1]
cnt = 0
t = int(input())
for i in range(t):
    nx, ny = x + dx[d], y + dy[d]
    if i == t - 1:
        break
    if 0<= nx <= h and 0<= ny <= w:
        x = nx
        y = ny
    else:
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]
        x = nx
        y = ny
print(x, y)
#시간 초과
import sys
input = sys.stdin.readline
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

nx = (p + t) // w
ny = (q + t) // h
if nx % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w
    
if ny % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h
print(x, y)