import sys
input = sys.stdin.readline

N = int(input())
bulb = [-1] + list(map(int, input().split()))
for _ in range(int(input())):
    gen, loc = map(int, input().split())
    M = N // loc
    if gen == 1:
        for i in range(M):
            if bulb[(i + 1) * loc] == 0:
                bulb[(i + 1) * loc] = 1
            else:
                 bulb[(i + 1) * loc] = 0
    else:
        a = list(i for i in range(loc - 1, -1, -1))
        b = list(i for i in range(loc + 1, N + 1))
        cnt = 0
        for index, c in enumerate(zip(a, b)):
            before, after = c[0], c[1]
            if bulb[before] != bulb[after]:
                break
            cnt += 1

        for i in range(loc - cnt, loc + cnt + 1):
            if bulb[i] == 0:
                bulb[i] = 1
            else:
                bulb[i] = 0
              
for i in range(1, N, 20):
    print(*bulb[i:i + 20])
    