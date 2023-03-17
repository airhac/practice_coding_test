# import sys
# from itertools import product
# from collections import defaultdict
# input = sys.stdin.readline
# n = int(input())
# dp = [defaultdict(int) for _ in range(n + 1)]
# def counter(dictionary):
#     cnt = 0
#     for k, v in dictionary.items():
#         cnt += v
#     return cnt
# for i in range(1, len(str(n)) + 1):    
#     for num in product(['4', '7'], repeat=i):
#         tmp = int(''.join(num))
        
#         if tmp <= n:
#             dp[tmp][tmp] += 1
#             for j in range(tmp + 1, n + 1):
#                 if dp[j - tmp]:
#                     temp = dp[j - tmp][tmp]
#                     temp += 1
#                     before_cnt = counter(dp[j - tmp])
#                     now_cnt = counter(dp[j])
#                     if not now_cnt:
#                         dp[j][tmp] = temp
#                     else:
#                         if before_cnt < now_cnt:
#                             dp[j] = dp[j - tmp]
#                             dp[j][tmp] = temp
# for an in dp[n]:
#     print(an, end=' ')
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
gold = []

def trace(k):
    if k == 0:
        return
    trace(visited[k])
    print(k - visited[k], end=' ')
for i in range(2, 128):
    temp =''
    b = bin(i)[2:]
    for j in range(1, len(b)):
        if b[j] == '0':
            temp += '4'
        else:
            temp += '7'
    gold.append(int(temp))
length = len(gold)
q = deque([0])
visited = [-1] * (1000001)
while q:
    now = q.popleft()
    
    if now == n:
        break
    for i in range(length):
        next = now + gold[i]
        if next > n:
            continue
        if visited[next] == -1:
            visited[next] = now
            q.append(next)
if visited[n] == -1:
    print(-1)
else:
    trace(n)