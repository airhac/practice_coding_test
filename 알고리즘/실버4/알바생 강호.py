import sys
input = sys.stdin.readline
n = int(input())
tips = [int(input()) for _ in  range(n)]
tips.sort(reverse=True)
answer = 0
for i in range(n):
    val = tips[i] - i 
    answer += (val if val > 0 else 0)
print(answer)