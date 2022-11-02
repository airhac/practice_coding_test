import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())

answers = defaultdict(list)
for i in range(N + 1):
    before = N
    after= i
    while True:
        diff = before - after
        if diff < 0:
            break
        answers[i].append(diff)
        before = after
        after = diff
answer = 0
for key, val in answers.items():
    if len(val) + 2 > answer:
        answer = len(val) + 2
        l = [N, key] + val
        
print(answer)
for i in l:
    print(i, end=' ') 