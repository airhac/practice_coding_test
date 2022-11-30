import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = str(input().rstrip())
    
    if s == s[::-1]:
        print('0')
        continue
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            front_tmp = s[:left] + s[left + 1:]
            back_tmp = s[:right] + s[right + 1:]
            if front_tmp == front_tmp[::-1]:
                print(1)
                break
            if back_tmp == back_tmp[::-1]:
                print(1)
                break
            print(2)
            break