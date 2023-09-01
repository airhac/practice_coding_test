import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())

q = [(0, n)]
heapq.heapify(q)
INF = int(1e9)

dp = [INF] * 100001
answer = INF
cnt = 0
while q:
    dist, now = heapq.heappop(q)

    if now == k:
        if answer >= dist:
            answer = dist
            cnt += 1
        else:
            break
        
    if now - 1 >= 0:
        if dp[now - 1] >= dist + 1:
            dp[now - 1] = dist + 1
            heapq.heappush(q, (dist + 1, now - 1))
    if now * 2 <= 100000:
        if dp[now * 2] >= dist + 1:
            dp[now * 2] = dist + 1
            heapq.heappush(q, (dist + 1, now * 2))
    if now + 1 <= 100000:
        if dp[now + 1] >= dist + 1:
            dp[now + 1] = dist + 1
            heapq.heappush(q, (dist + 1, now + 1))
        
print(answer)
print(cnt)