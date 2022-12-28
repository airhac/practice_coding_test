N=int(input())
arr=[[0,"A"],[0,"B"],[0,"C"],[0,"D"],[0,"E"],
       [0,"F"],[0,"G"],[0,"H"],[0,"I"],[0,"J"],]
neverZero=[0 for i in range(10)]
for i in range(N):
    word=input()
    size=len(word)
    for j in range(size):
        index=ord(word[size-1-j])-65
        if j==size-1:
            neverZero[index]=1
        arr[index][0]+=10**j

arr.sort(reverse=True)
# 0이 안되는거 확인(0까지 쓰일때만)0으로 시작되는 수가 없다 
# 마지막이 0이 안되는 수이면 다음 영이되는 수를 뒤로 보내면 됩니다. 그럼 0이 되지 않음
if arr[9][0]!=0:
    for i in range(9,-1,-1):
        if neverZero[ord(arr[i][1])-65]==0:
            temp=list(arr[i])
            arr.remove(temp)
            arr.append(temp)
            break

ans=0
for i in range(10):
    ans+=arr[i][0]*(9-i)
print(ans)