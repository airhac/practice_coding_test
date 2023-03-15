import sys
input = sys.stdin.readline
x, y = map(int, input().split())

left = 1
right = x

pre = y * 100 // x
answer = 0
if pre >=99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        percent = (y + mid) * 100 // (x + mid)
        if pre < percent:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

print(answer)
