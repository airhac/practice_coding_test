# import sys
# input = sys.stdin.readline
# n, m, x = map(int, input().split())
# INF = int(1e9)
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0
# for _ in range(m):
#     a, b, time = map(int, input().split())
#     graph[a][b] = time
 
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# answer = 0
# for i in range(1, n + 1):
#     taken = graph[i][x] + graph[x][i]
#     if answer < taken:
#         answer = taken
# print(answer)
#########플로이드 워셜은 시간초과
#최소경로를 구하는 다익스트라를 이용
import sys
import heapq
input = sys.stdin.readline
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
INF = int(1e9)
def dijkstra(start):
    distance = [INF] * (n + 1)
    q = [[0, start]]
    heapq.heapify(q)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            taken = dist + i[1]
            if distance[i[0]] > taken:
                distance[i[0]] = taken
                heapq.heappush(q, [taken, i[0]])
    return distance    


arr = dijkstra(x)
answer = 0
for i in range(1, n + 1):
    res = dijkstra(i)
    answer = max(answer, arr[i] + res[x])
print(answer)