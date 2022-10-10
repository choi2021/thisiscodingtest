n=int(input())
data=list(map(int,input().split()))
arr=[0]*(n+1)
dp=[0]*(n+1)

for i in range(1,n+1):
  arr[i]=data[i-1]

dp[1]=arr[1]

for i in range(2,n+1):
  dp[i]=arr[i]
  for j in range(1,i):
    dp[i]=max(dp[i],dp[i-j]+dp[j])

print(dp[n])