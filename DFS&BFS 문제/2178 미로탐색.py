from collections import deque

n,m=map(int,input().split())

graph=[]
for i in range(n):
	graph.append(list(map(int,list(input()))))

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y):
		q=deque([])
		q.append((x,y))
		while q:
			x,y=q.popleft()
			for i in range(4):
				nx,ny=x+dx[i],y+dy[i]
				if 0<=nx<n and 0<=ny<m:
					if graph[nx][ny]==1:
						graph[nx][ny]=graph[x][y]+1
						q.append((nx,ny))
		print(graph[n-1][m-1])
dfs(0,0)