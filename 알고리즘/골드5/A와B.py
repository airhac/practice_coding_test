# import sys
# s = str(input().split())
# t = str(input().split())
# while len(s) < len(t):
#     tmp = s
#     tmp = s + 'A'
#     if tmp == t:
#         print(1)
#         break
#     s = (s[::-1] + 'B')
#     if s == t:
#         print(1)
#         break
# print(0)
######
import sys
s = list(input().rstrip())
t = list(input().rstrip())
while t:
    if t[-1] == 'A':
        t.pop()
        
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        print(1)
        break
if not t:
    print(0)