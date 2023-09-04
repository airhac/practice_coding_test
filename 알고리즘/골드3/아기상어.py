import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
request = True

shark_x = 0
shark_y = 0
baby_shark_size = 2
#아기 상어의 위치 
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x = i
            shark_y = j
            graph[i][j] = 0
            break
cnt = 0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def check(size, i, j):
    q = [[0, i, j]]
    heapq.heapify(q)
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1
    INF = int(1e9)
    min_dist = INF
    temp = []
    while q:
        dist, x, y = heapq.heappop(q)    

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if 0 < graph[nx][ny] < size:
                    if min_dist == INF: # 처음 발견한 것보다 거리가 멀어지는 경우 바로 return
                        min_dist = dist
                    elif dist > min_dist:
                        return temp
                    temp.append((nx, ny, dist + 1))
                #자기 자신보다 크기가 큰물고기가 있는 칸은 지나 갈 수 없다
                if graph[nx][ny] > size:
                    continue
                heapq.heappush(q, (dist + 1, nx, ny))
    #더 이상 먹을 물고기가 없을때 엄마한테 요청
    return temp

answer = 0

while True:
    
    #우선 가장 가까에 먹을 수 있는 물고기가 있는지 확인  
    fishes = check(baby_shark_size, shark_x, shark_y)
    
    if len(fishes) == 0:
        print(answer)
        break
    fishes.sort()
    shark_x, shark_y, move_time = fishes[0]
    
    cnt += 1
    if cnt == baby_shark_size:
        baby_shark_size += 1
        cnt = 0
    
    # 물고기 한마리를 먹은거임
    graph[shark_x][shark_y] = 0
    answer += move_time



