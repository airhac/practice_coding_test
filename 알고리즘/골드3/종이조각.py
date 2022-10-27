import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]
for g in graph:
    print(g)
def solution(graph, N, M):
    result = 0
    # 2 ** N * M 경우를 다 고려
    for i in range(1 << N * M):
        tot = 0
        #가로로 잘라진 경우를 모두 찾아 tot에 더합니다.
        for row in range(N):
            temp = 0
            for col in range(M):
                idx = row * M + col
                if i & (1 << idx) != 0: temp = temp * 10 + graph[row][col]
                else:
                    tot += temp
                    temp = 0
            tot += temp
        for col in range(M):
            temp = 0
            for row in range(N):
                idx = row * M + col
                if i & (1 << idx) == 0: temp = temp * 10 + graph[row][col]
                else:
                    tot += temp
                    temp = 0
            tot += temp
        result = max(result, tot)
    return result

print(solution(graph, N, M))
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
# for a in arr:
#     print(a)
    
# def bf():
#   result = 0
#   for i in range(1 << N * M):
#       total = 0
#       for row in range(N):
#           srow = 0
#           for col in range(M):
#               idx = row * M + col
#               if i & (1 << idx) != 0: srow = srow * 10 + arr[row][col]
#               else:
#                   total += srow
#                   srow = 0
#           total += srow

#       for col in range(M):
#           scol = 0
#           for row in range(N):
#               idx = row * M + col
#               if i & (1 << idx) == 0: scol = scol * 10 + arr[row][col]
#               else:
#                   total += scol
#                   scol = 0
#           total += scol
#       result = max(result, total)
#   return result

# print(bf())