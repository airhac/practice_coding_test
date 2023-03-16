import sys
input = sys.stdin.readline
n, k = map(int, input().split())
def bfs(n, k):
    length = len(str(n))
    result = set([str(n)])
    for _  in range(k):
        arr = set()
        for res in result:
            for i in range(1, length):
                for j in range(i):
                    temp = list(str(res))
                    if j != 0 or int(temp[i]) != 0:
                        temp[i], temp[j] = temp[j], temp[i]
                        s = int(''.join(temp))
                        if s not in arr:
                            arr.add(s)
        result = arr
    return result
answer = bfs(n, k)
if answer:
    print(max(bfs(n, k)))
else:
    print(-1)