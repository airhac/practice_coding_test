import sys
input = sys.stdin.readline
n = int(input())
car_in = [input() for _ in range(n)]
car_out = [input() for _ in range(n)]
answer = 0
for i in range(1, n):
    index = car_out.index(car_in[i])
    for car in car_in[:i]:
        if car in car_out[index + 1:]:
            answer += 1
            break
print(answer)