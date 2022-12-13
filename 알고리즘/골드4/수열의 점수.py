import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]
minus = []
plus = []
one = []
for i in range(n):
    if arr[i] <= 0:
        minus.append(arr[i])
    elif arr[i] > 1:
        plus.append(arr[i])
    else:
        one.append(arr[i])
minus.sort()
plus.sort(reverse=True)
answer = 0
if len(minus) % 2 != 0:
    for i in range(0, len(minus) - 1, 2):
        now, next =  minus[i], minus[i + 1]
        answer += (now * next)
    answer += minus[-1]
else:
    for i in range(0, len(minus), 2):
        now, next =  minus[i], minus[i + 1]
        answer += (now * next)
if len(plus) % 2 != 0:
    for i in range(0, len(plus) - 1, 2):
        now, next =  plus[i], plus[i + 1]
        answer += (now * next)
    answer += plus[-1]
else:
    for i in range(0, len(plus), 2):
        now, next =  plus[i], plus[i + 1]
        answer += (now * next)
answer += sum(one)
print(answer)