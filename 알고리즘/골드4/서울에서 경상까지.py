import sys
from collections import defaultdict
input = sys.stdin.readline
n, k = map(int, input().split())
walking = [0] * n
cycling = [0] * n
for i in range(n):
    w1, w2, c1, c2 = map(int, input().split())
    walking[i] = (w1, w2)
    cycling[i] = (c1, c2)
# DP[i][j] i구간을 j시간까지 가는데까지의 최대 모금 금액
dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[1][walking[0][0]] = max(walking[0][1], dp[1][walking[0][0]])
dp[1][cycling[0][0]] = max(cycling[0][1], dp[1][cycling[0][0]])

for i in range(2, n + 1):
    w_t, w_c = walking[i - 1]
    c_t, c_c = cycling[i - 1]
    for j in range(k + 1):
        if dp[i - 1][j] == 0:
            continue
        if j + w_t <= k: #현재 시간 
            dp[i][j + w_t] = max(dp[i][j + w_t], w_c + dp[i - 1][j])
        if j + c_t <= k:
            dp[i][j + c_t] = max(dp[i][j + c_t], c_c + dp[i - 1][j])
answer = 0
for i in range(k + 1):
    answer = max(answer, dp[n][i])
print(answer)              
##########33

import sys


"""
# DP[i][j] i구간을 j시간까지 가는데까지의 최대 모금 금액
냅색(배낭)문제임!
혼자 풀 수 있어야 한다!
"""

# N, K = map(int, input().split())
# walking = [0] * N
# cycling = [0] * N
# for i in range(0, N):
#     walk_t, walk_c, cycle_t, cycle_c = map(int, input().split())
#     #             시간,  금액
#     walking[i] = (walk_t, walk_c)
#     cycling[i] = (cycle_t, cycle_c)

# # 초깃값 세팅
# # DP[i][j] i구간을 j시간까지 가는데까지의 최대 모금 금액
# DP = [[0] * (K+1) for _ in range(0, N+1)]
# DP[1][walking[0][0]] = max(DP[1][walking[0][0]], walking[0][1])
# # 위에 walking에서 동일한 시간에서 더 많은 금액을 가져오는 input이 들어올 수도 있다. (예외처리)
# DP[1][cycling[0][0]] = max(DP[1][cycling[0][0]], cycling[0][1])

# # 2부터 진행, N이 최대 100까지이므로 이런식의 로직도 충분히 가능!
# for i in range(2, N+1):
#     walk_time, walk_cost = walking[i-1]
#     cycle_time, cycle_cost = cycling[i-1]
#     for j in range(0, K+1):
#         # DP[i-1][j] 값이 0이라면 체크할 필요 없다. 의미없는 데이터인것
#         if DP[i-1][j] == 0:
#             continue
#         # 각 케이스 (걷기, 자전거)를 합한 시간이 K시간을 초과하지 않을 때에만, 
#         # 이전구간에서, 현재구간 걷기 // 이전구간에서 현재구간 자전거 각각 max값을 체크
#         if (j+walk_time) <= K:
#             DP[i][j+walk_time] = max(DP[i][j+walk_time], DP[i-1][j]+walk_cost)
#         if (j+cycle_time) <= K:
#             DP[i][j+cycle_time] = max(DP[i][j+cycle_time], DP[i-1][j]+cycle_cost)

# answer = 0
# # N번째 구간까지 도달하고 나서, K시간까지 순회하며 최댓값 찾기 (충분히 가능한 로직)
# for i in range(0, K+1):
#     answer = max(answer, DP[N][i])
# print(answer)
##########
# import sys

# # go : 현재 idx번째 경로에서 남은 시간이 total일 때 얻을 수 있는 최대 모금액을 리턴하는 함수
# def go(idx, total):
#     # 시간 예외 처리
#     if total < 0:
#         return -9876543210
#     # Base case : 경산까지 도달한 경우
#     if idx == n:
#         return 0
#     # Memoization
#     if dp[idx][total] != -1:
#         return dp[idx][total]
#     # 점화식
#     dp[idx][total] = max(go(idx + 1, total - arr[idx][0]) + arr[idx][1], go(idx + 1, total - arr[idx][2]) + arr[idx][3])
#     return dp[idx][total]

# # 입력부 및 정답출력
# n, k = map(int, sys.stdin.readline().split())
# dp = [[-1] * (k + 1) for _ in range(n)]
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(go(0, k))