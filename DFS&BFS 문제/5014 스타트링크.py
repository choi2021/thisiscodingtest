from collections import deque

f,s,g,u,d=map(int,input().split())
INF=int(1e9)
visited=[False]*(f+1)

def bfs(start):
	visited[start]=0
	q=deque()
	q.append((0,start))
	while q:
		num,pos=q.popleft()
		if pos==g:
			return num
		for i in [u,-d]:
			npos=pos+i
			if 1<=npos<f+1 and not visited[npos]:
				visited[npos]=True
				q.append((num+1,npos))
	return "use the stairs"
print(bfs(s))