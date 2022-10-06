import sys
input = sys.stdin.readline
N, K, P, X = map(int, input().split())

num_dict = { '0' : 0b1110111,
             '1' : 0b0010010,
             '2' : 0b1011101,
             '3' : 0b1011011,
             '4' : 0b0111010,
             '5' : 0b1101011,
             '6' : 0b1101111,
             '7' : 0b1010010,
             '8' : 0b1111111,
             '9' : 0b1111011}
cnt = 0
for i in range(1, N + 1):
    s = str(i)
    num = 0
    s = str(i).zfill(K)
    x = str(X).zfill(K)
    for j in range(K):
        a = s[j]
        b = x[j]
        c = num_dict[a] ^ num_dict[b]
        num += bin(c).count('1')
    if num <= P:
        cnt += 1
print(cnt - 1)