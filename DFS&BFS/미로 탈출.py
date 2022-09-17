from collections import deque

N,M=map(int,input().split())
graph=[]
for i in range(N):
  graph.append(list(map(int,input())))

dx=[1,0]
dy=[0,1]

def dfs(x,y):
  q=deque()
  q.append((x,y))
  while q:
    px,py=q.popleft()
    for i in range(2):
      nx=px+dx[i]
      ny=py+dy[i]
      if nx<0 or nx>=N or ny<0 or ny>=M or graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[px][py]+1
        q.append((nx,ny))
  print(graph)
  return graph[N-1][M-1]

print(dfs(0,0))