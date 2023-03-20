import sys
input = sys.stdin.readline
a, b = input().rstrip().split()
max_num = max(len(a), len(b))
min_num = min(len(a), len(b))
answer = []
for i in range(max_num - min_num + 1):
    cnt = 0
    if len(a) > len(b):
        for j in range(min_num):
            if a[j + i] != b[j]:
                cnt += 1
    else:
        for j in range(min_num):
            if a[j] != b[j + i]:
                cnt += 1
    answer.append(cnt)
print(min(answer))