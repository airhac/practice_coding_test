import sys
input = sys.stdin.readline
n = int(input())
start = 1
end = 1
answer = []
while start < 100000 and end < 100000:
    diff = end ** 2 - start ** 2
    if diff == n:
        answer.append(end)
        end += 1
    if diff < n:
        end += 1
    elif diff > n:
        start += 1
        
if not answer:
    print(-1)
else:
    for a in answer:
        print(a)