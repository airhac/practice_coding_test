def solution(grid):
    answer = []
    n = len(grid)
    m = len(grid[0])
    graph = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    dx, dy = [-1, 0, 1, 0], [0, -1, 0 , 1]
    def cycle(x, y, d):
        cnt = 0
        while not graph[x][y][d]:
            graph[x][y][d] = True
            
            x = (x + dx[d]) % n
            y = (y + dy[d]) % m
            if grid[x][y] == 'L': d = (d + 1) % 4
            elif grid[x][y] == 'R': d = (d - 1) % 4
            cnt+=1
        return cnt

    for i in range(n):
        for j in range(m):
            for d in range(4):
                if not graph[i][j][d]:
                    res = cycle(i, j, d)
                    answer.append(res)
    answer.sort()
    return answer
##다른 풀이(사이클이 완성되지 않는경우도 생각 해주는 풀이)
def solution(grid):
    answer = []
    n = len(grid)
    m = len(grid[0])
    graph = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    
    dx, dy = [-1, 0, 1, 0], [0, -1, 0 , 1]
    def cycle(sx, sy, sd):
        cnt = 0
        x, y, d = sx, sy, sd
        graph[x][y][d] = True
        
        while True:
            x = (x + dx[d]) % n
            y = (y + dy[d]) % m
            cnt+=1
            
            if grid[x][y] == 'L':
                d = (d + 1) % 4
            elif grid[x][y] == 'R':
                d = (d - 1) % 4
            #사이클을 돌았을때 시작한 위치와 방향과 다르면 사이클이 돌지 않는다는 경우
            if graph[x][y][d]:
                if (x, y, d) == (sx, sy, sd):
                    return cnt
                else:
                    return 0
            graph[x][y][d] = True
    
    for i in range(n):
        for j in range(m):
            for d in range(4):
                if not graph[i][j][d]:
                    res = cycle(i, j, d)
                    if res != 0:
                        answer.append(res)
    answer.sort()
    return answer