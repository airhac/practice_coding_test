import sys
input = sys.stdin.readline
n = int(input())
now = list(input().rstrip())
target = list(input().rstrip())
def change(temp):
    temp[0] = str(1 - int(temp[0]))
    temp[1] = str(1 - int(temp[1]))
    cnt = 1
    for i in range(1, len(temp)):
        if target[i - 1] != temp[i - 1]:
            cnt += 1
            temp[i - 1] = str(1 - int(temp[i - 1]))
            temp[i] = str(1 - int(temp[i]))
           
            if i < len(temp) - 1:
                temp[i + 1] = str(1 - int(temp[i + 1]))
    if temp == target:
        return cnt
    return 100001
def not_change(temp):
    cnt = 0
    for i in range(1, len(temp)):
        if target[i - 1] != temp[i - 1]:
            cnt += 1
            temp[i - 1] = str(1 - int(temp[i - 1]))
            temp[i] = str(1 - int(temp[i]))
           
            if i < len(temp) - 1:
                temp[i + 1] = str(1 - int(temp[i + 1]))
    if temp == target:
        return cnt
    return 100001
arr1 = change(now[:])
arr2 = not_change(now[:])
answer = min(arr1, arr2)
if answer == 100001:
    print(0)
else:
    print(answer)