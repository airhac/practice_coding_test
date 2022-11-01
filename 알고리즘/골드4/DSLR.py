import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    start, end = map(int, input().split())
    visited = [0] * 10000
    visited[start] = 1
    
    q = deque([(start, '')])
    
    while q:
        num, s = q.popleft()
        
        if end == num:
            answer = s
            break
            
        c_num = (num * 2) % 10000
        if not visited[c_num]:
            visited[c_num] = 1
            q.append((c_num, s + 'D'))
         
        c_num = (num - 1) % 10000
        if not visited[c_num]:
            visited[c_num] = 1
            q.append((c_num, s + 'S'))
            
        c_num = (10 * num + (num // 1000)) % 10000 
        if not visited[c_num]:
            visited[c_num] = 1
            q.append((c_num, s + 'L'))
            
        c_num = ((num // 10) + (num % 10) * 1000) % 10000
        if not visited[c_num]:
            visited[c_num] = 1
            q.append((c_num, s + 'R'))
        
    print(s)   
             
    