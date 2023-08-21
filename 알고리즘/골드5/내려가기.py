#메모리 초과함
# import sys
# input = sys.stdin.readline
# n = int(input())
# #앞이 max 뒤가 min

# arr = [list(map(int, input().split())) for _ in range(n)]
# temp = [[i, i] for i in arr[0]]

# for i in range(1, n):
#     for j in range(3):
#         if j == 0:
#             temp[j][0] = max(arr[i][0] + temp[j][0], arr[i][1] + temp[j][0])
#             temp[j][1] = min(arr[i][0] + temp[j][1], arr[i][1] + temp[j][1])
#         elif j == 1:
#             temp[j][0] = max(arr[i][0] + temp[j][0], arr[i][1] + temp[j][0], arr[i][2] + temp[j][0])
#             temp[j][1] = min(arr[i][0] + temp[j][1], arr[i][1] + temp[j][1], arr[i][2] + temp[j][1])
#         else:
#             temp[j][0] = max(arr[i][1] + temp[j][0], arr[i][2] + temp[j][0])
#             temp[j][1] = min(arr[i][1] + temp[j][1], arr[i][2] + temp[j][1])

# print(max(temp[0][0], temp[1][0], temp[2][0]), min(temp[0][1], temp[1][1], temp[2][1]))
### 메모리 초과 안함
import sys
input = sys.stdin.readline
n = int(input())
#앞이 max 뒤가 min

arr = list(map(int, input().split()))
max_dp = arr
min_dp = arr

for _ in range(n - 1):
    temp = list(map(int, input().split()))
    max_dp = [temp[0] + max(max_dp[0], max_dp[1]), temp[1] + max(max_dp), temp[2] + max(max_dp[1], max_dp[2])]
    min_dp = [temp[0] + min(min_dp[0], min_dp[1]), temp[1] + min(min_dp), temp[2] + min(min_dp[1], min_dp[2])]

print(max(max_dp), min(min_dp))