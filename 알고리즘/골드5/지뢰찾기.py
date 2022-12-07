import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr_cnt = list(map(int, list(input().rstrip())))
    arr = list(input().rstrip())
    answer = 0
    for i in range(n):
        if i == 0:
            if arr_cnt[i] != 0 and arr_cnt[i + 1] != 0:
                arr_cnt[i] -= 1
                arr_cnt[i + 1] -= 1
                answer += 1
        elif i == n - 1:
            if arr_cnt[i] != 0 and arr_cnt[i - 1] != 0:
                arr_cnt[i] -= 1
                arr_cnt[i - 1] -= 1
                answer += 1
        else:
            if arr_cnt[i] != 0 and arr_cnt[i - 1] != 0 and arr_cnt[i + 1] != 0:
                arr_cnt[i + 1] -= 1
                arr_cnt[i] -= 1
                arr_cnt[i - 1] -= 1
                answer += 1
    print(answer)