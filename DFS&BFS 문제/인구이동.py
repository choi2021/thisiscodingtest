# 내풀이: pypy3로는 풀리지만 그냥하면 80퍼에서 시간초과가 나
# from collections import deque

# n,l,r=map(int,input().split())
# graph=[]
# for i in range(n):
#   graph.append(list(map(int,input().split())))

# dx=[1,0,-1,0]
# dy=[0,1,0,-1]

# def find_union():
#   for i in range(n):
#     for j in range(n):
#       for k in range(4):
#         nx=i+dx[k]
#         ny=j+dy[k]
#         if 0<=nx<n and 0<=ny<n:
#           diff=abs(graph[i][j]-graph[nx][ny])
#           if l<=diff<=r:
#             return True
#   return False
  

# def bfs(x,y,visited):
#   q=deque([(x,y)])
#   visited[x][y]=True
#   total=graph[x][y]
#   union=[(x,y)]
#   while q:
#     x,y=q.popleft()
#     for i in range(4):
#       nx=x+dx[i]
#       ny=y+dy[i]
#       if 0<=nx<n and 0<=ny<n:
#         if l<=abs(graph[x][y]-graph[nx][ny])<=r and visited[nx][ny]==False:
#           total+=graph[nx][ny]
#           union.append((nx,ny))
#           visited[nx][ny]=True
#           q.append((nx,ny))
#   for x,y in union:
#     graph[x][y]=total//len(union)


# num=0

# while find_union():
#   visited=[[False]*n for _ in range(n)]
#   for i in range(n):
#     for j in range(n):
#       if visited[i][j]!=True:
#         bfs(i,j,visited)

#   num+=1
# print(num)

from collections import deque

n,l,r=map(int,input().split())

graph=[]

for _ in range(n):
  graph.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
result=0

def process(x,y,index):
  united=[]
  united.append((x,y))
  q=deque()
  q.append((x,y))
  union[x][y]=index
  summary=graph[x][y]
  count=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
        if l<=abs(graph[nx][ny]-graph[x][y])<=r:
          q.append((nx,ny))
          union[nx][ny]=index
          summary+=graph[nx][ny]
          count+=1
          united.append((nx,ny))
  for i,j in united:
    graph[i][j]=summary//count
  return count

total_count=0

while True:
  union=[[-1]*n for _ in range(n)]
  index=0
  for i in range(n):
    for j in range(n):
      if union[i][j]==-1:
        process(i,j,index)
        index+=1
  if index==n*n:
    break
  total_count+=1