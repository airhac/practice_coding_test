import sys
input = sys.stdin.readline
n = int(input().rstrip())
f = int(input().rstrip())
num = (n // 100) * 100 % f
print(str(f - num if num != 0 else num).zfill(2))