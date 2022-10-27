# import sys
# input = sys.stdin.readline
# n = int(input())
# words = input().strip()
# boj = 'BOJ'

# cnt = 0
# loc = 0
# tot = 0
# for index in range(n):
#     if words[index] == boj[cnt % 3]:
#         cnt += 1
#         tot += (index - loc) ** 2
#         loc = index
    
# if loc != n - 1:
#     print(-1)
# else:
#     print(tot)
#그리디로 풀려고 했으나 처음부터 거리가 최소인거만 고르게 되면 뒤에가 최대가 되어버린 경우가 생깁니다. 
#그래서 모든 경우를 고려해줘야한다고 생각했습니다.
import sys
input = sys.stdin.readline
n = int(input())
words = input().strip()
INF = int(1e9)
dp = [INF] * n
dp[0] = 0

def pre(now_node):
    if now_node == 'B':
        return 'J'
    elif now_node == 'O':
        return 'B'
    else:
        return 'O'
    
for i in range(1, n):
    for j in range(i):
        if words[j] == pre(words[i]):
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
print(dp[n - 1] if dp[n - 1] != INF else -1)
