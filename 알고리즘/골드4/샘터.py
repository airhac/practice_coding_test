import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
spring = list(map(int, input().split()))
visited = set()
q = deque()
for i in spring:
    q.append([i, 1])
    visited.add(i)
    
unfort = 0
built = 0
while q:
    now, dist = q.popleft()
    for i in [-1, 1]:
        nd = now + i
        if nd in visited:
            continue
        visited.add(nd)
        unfort += dist
        built += 1
        q.append([nd, dist + 1])
        if built == k:
            q = []
            break
print(unfort)
        