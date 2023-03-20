import sys
input = sys.stdin.readline
n = int(input())
arr = set()
for _ in range(n):
    string = input().split()
    c = True
    res = ''
    for s in range(0, len(string)):
        f = string[s][0].lower() 
        if f not in arr:
            string[s] = '[' + string[s][0] + ']' + string[s][1:]
            arr.add(f)
            c = False
            break
    else:
        if c:
            for s in range(0, len(string)):
                for i in range(1, len(string[s])):
                    low_word = string[s][i].lower()
                    if low_word not in arr:
                        string[s] = string[s][:i] + '[' + string[s][i] + ']' + string[s][i + 1:]
                        arr.add(low_word)
                        c = False
                        break
                if not c:
                    break
    for s in string:
        print(s, end=' ')
    print()
    