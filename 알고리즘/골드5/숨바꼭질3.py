# import sys
# from collections import deque
# input = sys.stdin.readline
# start, end = map(int, input().split())

# q = deque([(0, start)])
# answer = 0
# while q:
#     dist, now = q.popleft()
#     if now == end:
#         answer = dist
#         break
#     for i in [-1, 1, 0]:
#         if i != 0:
#             q.append((dist + 1, now + i))
#         else:
#             q.append((dist, 2 * now))
# print(q)
# print(answer)
#bfs로 풀경우 메모리초과 발생
import sys
import heapq
input = sys.stdin.readline
start, end = map(int, input().split())
INF = int(1e9)
dp = [INF] * 100001
dp[start] = 0
q = [(dp[start], start)]
heapq.heapify(q)

while q:
    dist, now = heapq.heappop(q)
    if dp[now] < dist:
        continue
    if now <= 50000:
        if dist < dp[now * 2]:
            dp[now * 2] = dist
            heapq.heappush(q, (dist, 2 * now))
    if now < 10 ** 5:
        if dist + 1 < dp[now + 1]:
            dp[now + 1] = dist + 1
            heapq.heappush(q, (dist + 1, now + 1))
    if 0 < now:
        if dist + 1 < dp[now - 1]:
            dp[now - 1] = dist + 1
            heapq.heappush(q, (dist + 1, now - 1))
print(dp[end])
