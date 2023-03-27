import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
q = deque(range(1, n + 1))
answer = 0
for num in arr:
    right = len(q) - q.index(num)
    left = q.index(num)
    if left <= right:
        while q[0] != num:
            tmp = q.popleft()
            q.append(tmp)
        q.popleft()
        answer += left
    else:
        while q[0] != num:
            tmp = q.pop()
            q.appendleft(tmp)
        q.popleft()
        answer += right
print(answer)