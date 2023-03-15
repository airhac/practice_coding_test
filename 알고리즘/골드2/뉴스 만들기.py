# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# #입력받는 부분
# N = int(input())
# bose_info = list(map(int, input().split()))
# #트리로 만들어 준다.
# tree = defaultdict(list)
# for me, bose in enumerate(bose_info):
#     if bose != -1:
#         tree[bose].append(me)

# #dp[i] : i번째 노드를 루트로 하는 서브트리에 뉴스를 전달하는데 필요한 최대 시간
# dp = [0 for _ in range(N)]

# def dfs(me):
#     temp=[]
    
#     for under in tree[me]:# 내 부하들을 대상으로
#         dfs(under)
#         temp.append(dp[under])
    
#     if temp: 
#         temp.sort(reverse=True) 
#         next_time = [temp[i] + i + 1 for i in range(len(temp))] 
#         dp[me] = max(next_time)

# dfs(0)
# print(dp[0])
import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
boses = list(map(int, input().split()))

trees = defaultdict(list)
for idx, bose in enumerate(boses):
    trees[bose].append(idx)
dp = [0] * (n + 1)   
def dfs(me):
    temp = []
    
    for load in trees[me]:
        dfs(load)
        temp.append(dp[load])
    if temp:
        temp.sort(reverse=True)
        arr = [temp[i] + i + 1 for i in range(len(temp))]
        dp[me] = max(arr)
dfs(0)
print(dp[0])