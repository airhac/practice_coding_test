import sys
input = sys.stdin.readline
width, height = map(int, input().split())
w, h = [], []
for _ in range(int(input())):
    bol, length = map(int, input().split())
    if bol == 0:
        h.append(length)
    else:
        w.append(length)
w.sort()
h.sort()
w_diff = []
h_diff = []
w = [0] + w
for i in range(1, len(w)):
    diff = w[i] - w[i - 1]
    w_diff.append(diff)
w_diff.append(width - w[-1])
h = [0] + h
for i in range(1, len(h)):
    diff = h[i] - h[i - 1]
    h_diff.append(diff)
h_diff.append(height - h[-1])
answer = 0
for i in w_diff:
    for j in h_diff:
        answer = max(answer, i * j)
print(answer)
##투포인터를 통해 각각의 리스트를 돌며 최대 크기 사각현의 넓이를 구함
import sys
input = sys.stdin.readline
width, height = map(int, input().split())
w, h = [0, width], [0,  height]
for _ in range(int(input())):
    bol, length = map(int, input().split())
    if bol == 0:
        h.append(length)
    else:
        w.append(length)
w.sort()
h.sort()
answer = 0
for i in range(len(w) - 1):
    for j in range(len(h) - 1):
        temp = (w[i + 1] - w[i]) * (h[j + 1] - h[j])
        answer = max(answer, temp)
print(answer)