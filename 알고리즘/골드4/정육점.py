import sys
input = sys.stdin.readline
n, m = map(int, input().split())
meats  = []
for _ in range(n):
    meats.append(list(map(int, input().split())))
meats = sorted(meats, key=lambda x : (x[1], -x[0]))
tot = sum(meats[i][0] for i in range(n))
if tot < m:
    print(-1)
    exit()
else:
    answer = sys.maxsize
    weight = 0
    same_price = 0
    
    for i in range(n):
        weight += meats[i][0]
        if i >= 1 and meats[i][1] == meats[i - 1][1]:
            same_price += meats[i][1]
        else:
            same_price = 0
            
        if weight >= m:
            answer = min(answer, meats[i][1] + same_price)
    print(answer)