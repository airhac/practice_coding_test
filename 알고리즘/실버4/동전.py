import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coin = []
for _ in range(N):
    num = int(input())
    if num <= K:
        coin.append(num)
cnt = 0    
for i in coin[::-1]:
    cnt += K // i
    K %= i
print(cnt)
########
N,K=map(int,input().split())
a=[int(input()) for _ in"A"*N]
s=0
for i in a[::-1]:s+=K//i;K%=i
print(s)