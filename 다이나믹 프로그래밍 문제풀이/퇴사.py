n=int(input())
t=[]
p=[]
for i in range(n):
	x,y=map(int,input().split())
	t.append(x)
	p.append(y)

max_value=0
dp=[0]*(n)

for i in range(n-2,-1,-1):
	if t[i]+i<=n:
		dp[i]=max(dp[i+1],dp[i+t[i]]+p[i])
	else:
		dp[i]=dp[i+1]

print(dp)