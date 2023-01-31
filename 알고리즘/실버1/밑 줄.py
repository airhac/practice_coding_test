import sys
input = sys.stdin.readline
n, m = map(int,input().split())
words = [input().rstrip() for _ in range(n)]
div_len, rest = divmod(m - sum(map(len, words)) , n - 1)
answer = words[0]
for i in range(1, n):
    if words[i][0].islower() and rest != 0:
        rest -= 1
        answer += ('_' * (div_len + 1) + words[i])
    elif i + rest == n:
        rest -= 1
        answer += ('_' * (div_len + 1) + words[i])
    else:
        answer += ('_' * div_len + words[i])
print(answer)