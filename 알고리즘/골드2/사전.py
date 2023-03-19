import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
dp = [[1] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
#k번째 수보다 n,m으로 구성 할 수 있는 문자열의 개수가 작으면 k번째 문자열을 알 수 없다는 뜻
#그러므로 -1을 출력합니다
if dp[n][m] < k:
    print(-1)
else:
    answer = ''
    while True:
        #둘중 하나라도 0이된다면 이제는 하나의 문자열 남은거만 뒤에 붙여주면 된다는 의미
        if n == 0 or m == 0:
            answer += 'a' * n
            answer += 'z' * m
            break
        #dp[n - 1][m]을 먼저 보는 이유는 n - 1 일때 'a'를 앞에 추가해준것
        #dp[n][m]에서 앞에 'a'가 있는 개수를 알 수 있습니다.
        res = dp[n - 1][m]
        #만약 앞에 'a'가 있는 개수보다 k가 작으면 앞에 'a'가 있다는 의미
        #만약 앞에 'a'가 있는 개수보다 k가 크면 앞에 'z'가 있다는 의미 입니다.
        if k <= res:
            answer += 'a'
            n -= 1
        else:
            answer += 'z'
            m -= 1
            #앞이 'z'일때 res값을 빼주는 이유는?
            #앞에 'a'를 갖는 값이 k에 포함 되어 있으니 그 부분도 같이 없애줍니다.
            #앞서는 문자열을 제거
            k -= res
    print(answer)