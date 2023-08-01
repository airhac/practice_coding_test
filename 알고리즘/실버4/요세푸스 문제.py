import sys
input = sys.stdin.readline
n, k = map(int, input().split())
now = 0
temp = [i for i in range(1, n + 1)]
answer = []
for _ in range(n):
    now = (now + (k - 1)) % len(temp)
    answer.append(temp.pop(now))
print("<" + ', '.join(list(map(str,answer))) + ">")