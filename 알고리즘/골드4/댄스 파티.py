import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
men = sorted(list(map(int, input().split())))
women = sorted(list(map(int, input().split())))
answer = 0
men_p_idx = bisect_left(men, 0)
women_p_idx = bisect_left(women, 0)
def find_group(answer, smaller, bigger):
    i = 0
    j = len(bigger) - 1
    
    while i < len(smaller) and j >= 0:
        if smaller[i] + bigger[j] < 0:
            i += 1
            j -= 1
            answer += 1
        else:
            j -= 1
    
    return answer
answer += find_group(answer, men[:men_p_idx], women[women_p_idx:])
print(answer)
answer += find_group(answer, women[:women_p_idx], men[men_p_idx:])

print(answer)