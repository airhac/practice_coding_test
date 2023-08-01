import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
answer = 0
for a in arr:
    if m - a in arr:
        answer += 1
print(answer)
# arr.sort()
# answer = 0
# start = 0
# end = n - 1
# while start <= end:
#     s = arr[start] + arr[end]
#     if s < m:
#         start += 1
#     elif s > m:
#         end -= 1    
#     else:
#         answer += 1
#         end -= 1
# print(answer)
