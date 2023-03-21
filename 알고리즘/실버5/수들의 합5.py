import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(i, n + 1):
        cnt += j
        if cnt == n:
            answer += 1
            break
        elif cnt > n:
            break
print(answer)