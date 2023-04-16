import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
start = 0
end = n - 1
answer = []
INF = int(1e10)
before = INF
while start < end:
    diff = arr[start] + arr[end]
    if abs(diff) <= before:
        answer .append([arr[start], arr[end]])
        before = abs(diff)
    if diff > 0:
        end -= 1
    else:
        start += 1
        
print(answer[-1][0], answer[-1][1])