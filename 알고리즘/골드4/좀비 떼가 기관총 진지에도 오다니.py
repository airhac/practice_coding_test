import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
cro, dmg = map(int, input().split())
bomb = int(input())
zombs = [int(input()) for _ in range(n)]
total_shoot = deque({})
cnt = 0
die = False
while cnt < n:
    while total_shoot and cnt >= total_shoot[0] + cro:
        total_shoot.popleft()
        
    if zombs[cnt] > len(total_shoot) * dmg + dmg:
        if bomb:
            bomb-=1
        else:
            die = True
            break
    else:
        total_shoot.append(cnt)
    cnt  += 1
    
if die:
    print('NO')
else:
    print('YES')
        