import sys
input = sys.stdin.readline
n = int(input())
answer = [0] * n
balls = [0] * 200001
arr = [list(map(int, input().split())) + [idx] for idx in range(n)]
arr.sort(key = lambda x : x[1])
tot = 0
j = 0
for i in range(n):
    while arr[j][1] < arr[i][1]:
        balls[arr[j][0]] += arr[j][1]
        tot += arr[j][1]
        j += 1
    answer[arr[i][2]] = tot - balls[arr[i][0]]
for a in answer:
    print(a)
    