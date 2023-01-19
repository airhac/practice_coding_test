# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     cho_value = int(input())
#     coins = []
#     answer = 0
#     k = 0
#     while (10 ** (2*k)) <= cho_value or (10 ** (2*k + 1)) <= cho_value or 25 * (10 ** (2 * k)) <= cho_value:
#         if (10 ** (2*k)) <= cho_value:
#             coins.append(10 ** (2*k))
#         if (10 ** (2*k + 1)) <= cho_value:
#             coins.append(10 ** (2*k + 1))
#         if 25 * (10 ** (2 * k)) <= cho_value:
#             coins.append(25 * (10 ** (2 * k)))
#         k += 1
#     print(coins)
#     for coin in coins[::-1]:
#         answer += cho_value // coin
#         cho_value %= coin
#     print(answer)
##############
import sys
input = sys.stdin.readline
coin = [1, 10, 25]
INF = int(1e9)
dp = [INF] * 100
dp[0] = 0
#1,10,25의 100배수인 동전들이 존재함으로 100안의 숫자들중 1,10,25로 만들수 있는 최소 동전 개수만 알면 
#그 이상의 숫자도 100으로 나누었을때 동전의 최소 개수를 알 수 있습니다.
for i in range(1, 100):
    for c in coin:
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)
#10의 자리수 이하는 1, 10, 25로 구할 수 있으며 1000의 자리수 이하는 100, 1000, 2500로 필요 최소 동전 개수를 알수 있습니다.
for _ in range(int(input())):
    cho_value = int(input())
    answer = 0
    while cho_value > 0:
        answer += dp[cho_value % 100]
        cho_value //= 100
    print(answer)