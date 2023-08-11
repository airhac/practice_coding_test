import sys
input = sys.stdin.readline

L, R = input().rstrip().split()
L_len = len(L)
R_len = len(R)
answer = 0
if L_len != R_len:
    print(answer)
else:
    for i in range(L_len):
        if L[i] == R[i]:
            if L[i] == '8':
                answer += 1
        else:
            break
    print(answer)