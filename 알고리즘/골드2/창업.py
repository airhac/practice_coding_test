import sys
from collections import deque
input = sys.stdin.readline

gu_apple = list(input().rstrip())
cube_lover = list(input().rstrip())

n = len(gu_apple)
answer = ['?'] * n
gu_apple.sort()
cube_lover.sort()
gu_apple =  deque(gu_apple[:(n + 1) // 2])
cube_lover = deque(cube_lover[n - n //2:n])
left = 0
right = n - 1
print(gu_apple)
print(cube_lover)
for i in range(n):
    # i가 홀수 이면 큐러브 턴
    if i % 2: 
        #큐러브의 제일 큰 수가 구사과의 문자가 작거나 같으면 큐러브의 작은수를 제일 오른쪽으로 놓는다
        if gu_apple and gu_apple[0] >= cube_lover[-1]:
            answer[right] = cube_lover.popleft()
            right -= 1
        #구사과의 문자가없거나 구사과의 제일 작은 문자가 큐러브의 제일 큰수보다 작은경우 제일 오른쪽에 제일 큰수를 넣습니다
        else:
            answer[left] = cube_lover.pop()
            left += 1
    # i가 짝수 이면 구사과 턴
    else:    
        #위의 상황과 반대
        #큐러브의 제일 작은수가 구사과의 제일 큰수 보다 크거나 같으면 구사과의 큰수를 answer의 현재 배치할수 있는 제일 오른쪽에 배치 해야 
        if cube_lover and gu_apple[0] >= cube_lover[-1]:
            answer[right] = gu_apple.pop()
            right -= 1
        else:
            answer[left] = gu_apple.popleft()
            left += 1
print(''.join(answer))