import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
s = 0
for i in range(N):
    s += arr[i]
    arr[i] = s
answer = -100
arr = [0] + arr
for i in range(K,N + 1):
    diff = arr[i] - arr[i - K]
    answer = max(answer, diff)
print(answer)