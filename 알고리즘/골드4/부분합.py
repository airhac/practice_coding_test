import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
tot = 0
start = 0
answer = int(1e9)
for i in range(n):
    tot += arr[i]
    while tot >= s:
        tot -= arr[start]
        answer = min(answer, (i + 1) - start)
        start += 1
print(answer)
    