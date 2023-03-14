import sys
input = sys.stdin.readline
x, y = map(int, input().split())

left = 1
right = 1000000000

pre = int(y / x * 100)
answer = 0
while left <= right:
    mid = (left + right) // 2
    percent = int((y + mid) / (x + mid) * 100)
    if pre < percent:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
if percent < pre:
    print(-1)
else:
    print(answer)
