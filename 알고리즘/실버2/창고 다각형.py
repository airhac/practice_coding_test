import sys
input = sys.stdin.readline
house = []
for _ in  range(int(input())):
    loc, col = map(int, input().split())
    house.append([col, loc])
house.sort(reverse=True)
front = house[0][1]
back = house[0][1]
roof = house[0][0]
for i in range(1, len(house)):
    if house[i][1] < front:
        roof += ((front - house[i][1]) * house[i][0])     
        front = house[i][1]
    elif house[i][1] > back:
        roof += ((house[i][1] - back) * house[i][0])     
        back = house[i][1]
print(roof)
####3
from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(input())
h = [0] * 1001

for _ in range(n):
    x, y = map(int, read().split())
    h[x] = y

highest_index = h.index(max(h))
now_max = 0
s = 0
for i in range(0, highest_index):
    if now_max < h[i]:
        now_max = h[i]
    s += now_max

now_max = 0
for i in range(1000, highest_index, -1):
    if now_max < h[i]:
        now_max = h[i]
    s += now_max

print(s+max(h))