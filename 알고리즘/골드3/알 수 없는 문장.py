import sys
INF = int(1e9)
input = sys.stdin.readline
s = input().rstrip()
n = int(input())
words = [list(input().rstrip()) for _ in range(n)]
length = len(s)
dp = [INF] * (len(s) + 1)
dp[0] = 0
# 현재 비교하고 싶은 문장에 같은 단어의 개수가 같은지 확인해 줍니다.
def compare_string(string1, string2):
    if len(string1) != len(string2):
        return False
    arr = [0] * 26
    str_len = len(string1)
    for loc in range(str_len):
        #현재 문자와 'a'의 차이인 위치에 단어 개수를 추가하고
        # string2에 있는 단어는 단어 개수를 빼주어 해당 단어가 같은게 있는지 확인해 줍니다. 
        arr[ord(string1[loc]) - 97] += 1
        arr[ord(string2[loc]) - 97] -= 1
    for l in range(26):
        if arr[l] != 0:
            return False
    return True
#서로다른 단어 위치의 개수를 확인 
def diff(string1, string2):
    count = 0
    for a, b in zip(string1, string2):
        if a != b:
            count+=1
    return count
for i in range(1, length + 1):
    part_of_s = []
    for j in range(i):
        part_of_s.append(s[j:i])
    split_l = len(part_of_s)
    for j in range(split_l):
        for k in range(n):
            if not compare_string(part_of_s[j], words[k]):
                continue
            diff_loc = diff(part_of_s[j], words[k])
            # j가 처음부터 j 까지의 글자 중 단어와 맞는 최소개수 이고  그 이후에 있는 모든 문장과 맞는 단어가 있으면 i에 
            # 앞에 값과 더한 값을 넣어줍니다. 그래서 j가 0이라는 거는 그 앞 즉 dp[j]가 없다는 것입니다.
            if j == 0:
                dp[i] = min(diff_loc, dp[i])
                continue
            dp[i] = min(dp[i], diff_loc + dp[j])
            
if dp[length] != INF:
    print(dp[length])
else:
    print(-1)