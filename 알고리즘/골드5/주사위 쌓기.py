import sys
n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
d = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}
answer = 0
#위에 올라오는 숫자의 시작
for i in range(1, len(dices[0]) + 1):
    arr = []
    start = i
    max_tot = 0
    for dice in dices:
        res = dice[:]
        idx = res.index(start)
        res.remove(start)
        across_index = d[idx]
        start = dice[across_index]
        res.remove(start)
        max_tot += max(res)
    answer = max(answer, max_tot)    
print(answer)