import sys
input = sys.stdin.readline
n, m = map(int, input().split())
meats  = []
for _ in range(n):
    kg, cost = map(int, input().split())
    meats.append((cost, kg))
meats.sort(key=lambda x: x[0], reverse=True)
answer = 2147483647
min_cost = 0
for i in range(n):
    if meats[i][1] <= m:
        min_cost += meats[i][0]
        answer = min(answer, min_cost)
        break
    else:
        answer = meats[i][0]
        
if answer + sum(meats[j][1] for j in range(i, n)) < m:
    print(-1)
else:
    print(answer)