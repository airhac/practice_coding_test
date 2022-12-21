import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n + 1)]
loc = 0
answer = 0
arr.sort()
truck = arr[-1][1]
q = [] 
for i in range(n + 1):
    now, gas = arr[i]
    dist = now - loc
    loc = now
    if truck < dist:
        while truck < dist:
            if len(q) > 0:
                truck += (-heapq.heappop(q))
                answer += 1
            else:
                answer = -1
                break
        if answer == -1:
            break
    truck -= dist
    heapq.heappush(q, -arr[i][1])
print(answer)