# n,k=map(int,input().split())
# graph=[]
# virus=[]
# temp=[]

# for i in range(n):
#   graph.append(list(map(int,input().split())))

# s,x,y=map(int,input().split())

# dx=[1,0,-1,0]
# dy=[0,1,0,-1]

# def spread(x,y):
#   for i in range(4):
#     nx=x+dx[i]
#     ny=y+dy[i]
#     if 0<=nx<n and 0<=ny<n:
#       if graph[nx][ny]==0:
#         graph[nx][ny]=graph[x][y]
#         temp.append((graph[x][y],nx,ny))

# def check_pos():
#   result=False
#   for i in range(n):
#     for j in range(n):
#       if graph[i][j]!=0:
#         result=True
#         virus.append((graph[i][j],i,j))
#   return result

# virus.sort(key=lambda x:x[0])

# for _ in range(s):
#   for i in virus:
#     num,px,py=i
#     spread(px,py)
#   virus=temp
#   temp=[]

# print(graph[x-1][y-1])

#책풀이 DFS를 이용해서 방문체크를 했어

from collections import deque

n,k=map(int,input().split())

graph=[]
data=[]

for i in range(n):
  graph.append(list(map(int,input().split())))
  for j in range(n):
    if graph[i][j]!=0:
      data.append((graph[i][j],0,i,j))

data.sort()
q=deque(data)

target_s,target_x,target_y=map(int,input().split())

dx=[-1,0,1,0]
dy=[0,1,0,-1]

while q:
  virus,s,x,y=q.popleft()
  if s==target_s:
    break
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<n and 0<=ny<n:
      if graph[nx][ny]==0:
        graph[nx][ny]=virus
        q.append((virus,s+1,nx,ny))
print(graph[target_x-1][target_y-1])