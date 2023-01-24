import sys
input = sys.stdin.readline
n, m = map(int, input().split())
price = [int(input()) for _ in range(m)]
price.sort()
answer = [0, 0]

for i in range(m):
    cnt = m - i
    if n >= cnt:
        if answer[1] < cnt * price[i]:
            answer[1] = cnt * price[i]
            answer[0] = price[i]
            
print(answer[0], answer[1])