import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
temp = [0] * (n + 1)
for i in range(n):
    temp[i + 1] = temp[i] + arr[i]
print(temp)
answer = 0 
for i in range(1, n):
    start, end = i, n
    while start <= end:
        mid = (start + end) // 2
        d = temp[mid] - temp[i - 1]
        re_d = temp[n] - d
        #반 시계 방향이 더 작은경우
        if d < re_d:start = mid + 1
        else:
            end = mid - 1
        answer = max(answer, min(d, re_d))
print(answer)