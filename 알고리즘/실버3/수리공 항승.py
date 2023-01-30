import sys
input = sys.stdin.readline
n, l = map(int, input().split())
broken = list(map(int, input().split()))
pipe = [0] * 1001

for b in broken:
    pipe[b] = 1
length = 0
answer = 0
for i in range(1, 1001):
    if pipe[i] == 1:
        length += 1
    else:
        if length == 0:
            continue
        elif length < l:
            answer += 1
        else:
            answer += (length // l + 1 if length % l != 0 else length // l)
            length = 0
if length:
    answer += (length // l + 1 if length % l != 0 else length // l)
print(answer)