import sys
input = sys.stdin.readline

s = str(input().rstrip())
p = str(input().rstrip())
stack = p[-1]
n = len(p) - 1
answer = 0
while n >= 0:
    if stack in s:
        stack = p[n] + stack
        n -= 1
    else:
        answer += 1
        stack = p[n + 1]
print(answer)