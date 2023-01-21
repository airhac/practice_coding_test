#이전 가게 최솟값, 섞어살때 최소값, 낱개로만 살떄 최소값을 구한다.
# INF = int(1e9)
# answer = INF
# brands = [list(map(int, input().split())) for _ in range(m)]
# for brand in brands:
#     bundle, single = brand
#     if n < 6:
#         answer = min(answer, n * single,((n // 6) * bundle) + (single * (n % 6)))
#     else:
#         answer = min(answer, bundle, n * single)
# print(answer)
################
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

bundles, singles = [], []
for _ in range(m):
    a = list(map(int, input().split()))
    bundles.append(a[0])
    singles.append(a[1])
bundles.sort()
singles.sort()
bundle = bundles[0]
single = singles[0]

if n < 6:
    print(min(bundle, single * n))
else:
    print(min(bundle * (n // 6 + 1), ((n // 6) * bundle) + (single * (n % 6)), single * n))
