import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
answer = []
for i in range(1, n):
    answer.append(sensors[i] - sensors[i - 1])
answer.sort()
print(answer[:n - k])