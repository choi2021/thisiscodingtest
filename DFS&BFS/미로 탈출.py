from collections import deque

N,M=map(int,input().split())

graph=[]

for _ in range(N):
  graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,+1]

def BFS(x,y):
  
  queue=deque()
  queue.append((x,y))
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<=-1 or ny<=-1 or nx>=N or ny>=M:
        continue
      if graph[nx][ny]==0:
        continue
      elif graph[nx][ny]==1: # 처음 방문하면 1 
        queue.append((nx,ny))
        graph[nx][ny]=graph[x][y]+1
  return graph[N-1][M-1]

print(BFS(0,0))
