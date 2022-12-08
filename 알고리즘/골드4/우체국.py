import sys
import math
input = sys.stdin.readline
vils = []
peoples = 0

n = int(input())
for i in range(n):
    vil, people = map(int, input().split())
    vils.append([vil, people])
    peoples += people
vils.sort(key=lambda x : x[0])

answer = 0
for i in range(n):
    answer += vils[i][1]
    if answer >= math.ceil(peoples/2):
        print(vils[i][0])
        break
        