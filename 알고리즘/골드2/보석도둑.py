import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
heapq.heapify(jewels)
print(jewels)
bags.sort()
answer = 0
put = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(put, -heapq.heappop(jewels)[1])
    if put:
        answer -= heapq.heappop(put)
    elif not jewels:
        break
print(answer)
        