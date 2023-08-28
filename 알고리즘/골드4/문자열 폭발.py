import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().strip()

bomb_check = len(bomb)

stack = []
for i in range(len(word)):
    stack.append(word[i])
    if len(stack) >= bomb_check:
        if ''.join(stack[-bomb_check:]) == bomb:
            for _ in range(bomb_check):
                stack.pop()
    
if stack:
    print(''.join(stack))
else:
    print('FRULA')