import sys
input = sys.stdin.readline
n, k  = map(int,input().split())
arr = list(map(int, input().split()))
teams = []
for i in range(1, n):
    teams.append(arr[i] - arr[i - 1])
teams.sort()
print(sum(teams[:n - k]))
      