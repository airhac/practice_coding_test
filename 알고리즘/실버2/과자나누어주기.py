import sys
input = sys.stdin.readline
M, N = map(int, input().split())
cookies = list(map(int, input().split()))
start = 1
end = max(cookies)
answer = 0
res = False
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(N):
        cnt += (cookies[i] // mid)
    if cnt >= M:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)