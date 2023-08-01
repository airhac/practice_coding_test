import sys
from math import ceil
input = sys.stdin.readline
n, c, w = map(int, input().split())
trees = [int(input()) for _ in range(n)]
profits = []

for L in range(1, max(trees) + 1):
    profit = []
    for tree in trees:
        profit.append(max(0, (tree // L) * L * w - ((ceil(tree / L) - 1) * c)))
    profits.append(sum(profit))
print(max(profits))