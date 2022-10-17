def solution(triangle):
	dp=triangle[:]
	n=len(dp)
	for i in range(1,n):
		for j in range(len(triangle[i])):
			if j==0:
				left=0
			else:
				left=dp[i-1][j-1]
			if j==len(triangle[i])-1:
				right=0
			else:
				right=dp[i-1][j]
			dp[i][j]=triangle[i][j]+max(left,right)
	return max(dp[-1])

triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)