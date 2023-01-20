import sys
input = sys.stdin.readline
N = int(input())
wrong_indent = list(map(int, input().split()))
correct_indent = list(map(int, input().split()))

diffs = [wrong_indent[i] - correct_indent[i] for i in range(N)]
answer = 0
check = 0
while any(diffs):
    #check가 0인경우는 이전도 0이다. check가 1인 경우는 이전인 경우가 추가, checkrk 2인 경우는 이전인 경우가 삭제
    for i in range(N):
        if diffs[i] == 0:
            check = 0
        elif diffs[i] > 0:
            if check != 1:
                answer += 1
                diffs[i] -= 1
                check = 1
            else:
                diffs[i] -= 1
        else:
            if check != 2:
                answer += 1
                diffs[i] += 1
                check = 2
            else:
                diffs[i] += 1
    check = 0
print(answer)