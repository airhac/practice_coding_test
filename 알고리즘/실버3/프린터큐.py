import sys
from collections import deque
input = sys.stdin.readline


t = int(input())
c = -1
for _ in range(t):
    n, m = map(int, input().split())
    docs = deque(list(map(int, input().split())))
    cnt = 0
    
    while docs:
        max_num = max(docs)
        temp = docs.popleft()
        m-=1
        
        if max_num == temp:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            docs.append(temp)
            if m < 0:
                m = len(docs) - 1