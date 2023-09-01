import sys
input = sys.stdin.readline
m = int(input())
d = 1000000007
answer = 0
def power(num, t):
    if t == 1:
        return num % d
    elif t % 2:
        return num * power(num, t - 1) % d
    else:
        p = power(num, t // 2)
        return p * p % d
for _ in range(m):
    n, s = map(int, input().split())
    answer += s * power(n, d - 2) % d
print(answer%d)