import sys
input = sys.stdin.readline
arr = []
ew = set([1, 2])
ns = set([3, 4])
n = int(input())
w = 0
h = 0
for _ in range(6):
    loc, length = map(int, input().split())
    if loc in ew:
        w = max(w, length)
    if loc in ns:
        h = max(h, length)
    arr.append([loc, length])
max_l = set([w, h])
res = 1
tot = w * h
for i in range(len(arr)):
    before = arr[i - 1][1] if i - 1 >= 0 else arr[-1][1]
    after = arr[i + 1][1] if i + 1 < len(arr) else arr[0][1]
    if (before + after) in max_l:
        res *= arr[i][1]
    
print((tot - res) * n)