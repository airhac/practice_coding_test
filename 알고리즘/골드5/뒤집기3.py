import sys
input = sys.stdin.readline
s = str(input().rstrip())
n = len(s)
i = 0
while i < n - 1:
    if s[i] > s[i + 1] and s[i + 1]  <= s[0]:
        s = s[:i + 1][::-1] + s[i + 1:]
        if s[i] >= s[i + 1]:
            s = s[:i + 2][::-1] + s[i + 2:]
    i += 1
print(s)