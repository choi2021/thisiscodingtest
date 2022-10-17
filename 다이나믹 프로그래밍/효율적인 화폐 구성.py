n,m=map(int,input().split())
INF=int(1e9)
coins=[]
for i in range(n):
  coins.append(int(input()))
dp=[INF]*(10001)
dp[0]=0
for i in range(n):#화폐단위를 돌면서
  for j in range(coins[i],m+1):
    if dp[j-coins[i]]!=10001:
      dp[j]=min(dp[j],dp[j-coins[i]]+1)

if dp[m]==INF:
  print(-1)
else:
  print(dp[m])