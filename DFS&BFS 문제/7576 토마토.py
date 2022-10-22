from collections import deque
m,n=map(int,input().split())
graph=[]
q=deque()
for i in range(n):
	arr=list(map(int,input().split()))
	graph.append(arr)
	for j in range(m):
		if arr[j]==1:
			q.append((0,i,j))

dx=[1,0,-1,0]
dy=[0,-1,0,1]

count=0
while q:
		day,x,y=q.popleft()
		count=day
		for i in range(4):
			nx,ny=x+dx[i],y+dy[i]
			if 0<=nx<n and 0<=ny<m:
				if graph[nx][ny]==0:
					graph[nx][ny]=1
					q.append((day+1,nx,ny))

result=True
for i in range(n):
	for j in range(m):
		if graph[i][j]==0:
			result=False

if result:
	print(count)
else:
	print(-1)