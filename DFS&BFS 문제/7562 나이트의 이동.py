from collections import deque
t=int(input())
for _ in range(t):
	n=int(input())
	x,y=map(int,input().split())
	target_x,target_y=map(int,input().split())

	dx=[-2,-1,1,2,2,1,-1,-2]
	dy=[1,2,2,1,-1,-2,-2,-1]
	visited = [[False] * n for i in range(n)]

	def bfs(x,y):
		q=deque()
		q.append((0,x,y))
		visited[x][y]=True
		while q:
			cnt,x,y=q.popleft()
			if x == target_x and y == target_y:
				return cnt
			for i in range(8):
				nx,ny=x+dx[i],y+dy[i]
				if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
					q.append((cnt+1,nx,ny))
					visited[nx][ny]=True


	print(bfs(x,y))