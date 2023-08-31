import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
# O(N log N)
# import sys

# def binarySearch(arr, left, right, value):
#     mid = (left + right) // 2
    
#     if left > right:
#         return -1
    
#     if arr[mid] < value <= arr[mid+1]:
#         return mid+1
    
#     if arr[mid] >= value:
#         return binarySearch(arr, left, mid-1, value)
    
#     if arr[mid] < value:
#         return binarySearch(arr, mid+1, right, value)

# if __name__ == "__main__":
#     N = int(input())

#     # 수열 A
#     A = [0]

#     # 길이가 i 인 증가하는 부분 수열 중 끝점의 최솟값
#     dp = [0] * (N+5)
#     dpLength = 1 # dp 배열의 현재 길이

#     A += list(map(int, sys.stdin.readline().strip().split()))

#     for i in range(1, N+1): # 1 ~ N
#         index = binarySearch(dp, 0, dpLength-1, A[i])
        
#         # dp에 값이 새로 추가되는 경우
#         if index == -1:
#             dp[dpLength] = A[i]
#             dpLength += 1
        
#         # 끝점의 최솟값을 바꾸는 경우
#         else:
#             dp[index] = A[i]
        
#     print(dpLength-1)