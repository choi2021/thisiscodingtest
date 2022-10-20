n=int(input())
arr=list(map(int,input().split()))

dp=[1]*n

for i in range(n):
	for j in range(i):
		if arr[j]<arr[i]:
			dp[i]=max(dp[i],dp[j]+1)

max_len=max(dp)
max_idx=dp.index(max_len)
temp=[]
while max_idx>=0:
	if dp[max_idx]==max_len:
		temp.append((arr[max_idx]))
		max_len-=1
	max_idx-=1
temp.reverse()
print(*temp)