import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
arr = [input().rstrip() for _ in range(n)]
d = defaultdict(int)
for a in arr:
    d[a] += 1
d = sorted(d.items(), key=lambda x : (x[1]), reverse=True)
print(d[0][0])