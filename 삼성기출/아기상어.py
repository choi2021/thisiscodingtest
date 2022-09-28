# BFS문제
#1.자기보다 크기가 큰쪽으로는 갈 수 없다
#2.작은 물고기는 먹을 수 있다
#3.같은 물고기는 지나갈 수 있다.
#4.먹은 물고기 개수=크기가 되면 크기가 커진다
#5.먹을 수 있는 물고기중 가장 가까운 물고기를 먹으러 간다.
#6.더이상 먹을 수 없을 때까지 반복한다. (v)

# from collections import deque
# n=int(input())
# graph=[]


# for i in range(n):
#   graph.append(list(map(int,input().split())))

# size=2
# eat=0
# dx=[1,0,-1,0]
# dy=[0,1,0,-1]
# result=0

# def search_fish():
#   for i in range(n):
#     for j in range(n):
#       if graph[i][j]==9:
#         continue
#       if graph[i][j]<size and graph[i][j]!=0:
#         return True
#   return False

# def find_start():
#   for i in range(n):
#     for j in range(n):
#       if graph[i][j]==9:
#         return (i,j)

# def bfs(graph,start):
#   global size,eat
#   time=[[0]*n for i in range(n)]
#   visited=[[False]*n for i in range(n)]
#   x,y=start
#   q=deque([start])
#   visited[x][y]=True
#   while q:
#     x,y=q.popleft()
#     for i in range(4):
#       nx=x+dx[i]
#       ny=y+dy[i]
#       if nx<0 or ny<0 or nx>=n or ny>=n:
#         continue
#       if graph[nx][ny]>size:
#         continue
#       elif graph[nx][ny]<=size and not visited[nx][ny]:
#         if graph[nx][ny]!=0:
#           eat+=1
#           if eat==size:
#             size+=1
#             eat=0
#           graph[nx][ny]=9
#           return time[nx][ny] 
#         q.append((nx,ny))
#         time[nx][ny]+=1
#         visited[nx][ny]=True


# while search_fish():
#   start=find_start()
#   print(bfs(graph,start))
# print(result)


#책풀이: 똑같이 BFS로 구현했어

from collections import deque
INF=int(1e9)

n=int(input())

array=[]
for i in range(n):
  array.append(list(map(int,input().split())))

now_size=2
nox_x,now_y=0,0

for i in range(n):
  for j in range(n):
    if array[i][j]==9:
      now_x,now_y=i,j
      array[now_x][now_y]=0

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs():
  dist=[[-1]*n for _ in range(n)]
  q=deque([(now_x,now_y)])
  dist[now_x][now_y]=0
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n:
        if dist[nx][ny]==-1 and array[nx][ny]<=now_size:
          dist[nx][ny]=dist[x][y]+1
          q.append((nx,ny))
  return dist

def find(dist):
  x,y=0,0
  min_dist=INF
  for i in range(n):
    for j in range(n):
      if dist[i][j]!=-1 and 1<=array[i][j]<now_size:
        if dist[i][j]<min_dist:
          x,y=i,j
          min_dist=dist[i][j]
  if min_dist==INF:
    return None
  else:
    return x,y,min_dist

result=0
ate=0

while True:
  value=find(bfs())
  if value==None:
    print(result)
    break
  else:
    now_x,now_y=value[0],value[1]
    result+=value[2]
    array[now_x][now_y]=0
    ate+=1
    if ate>=now_size:
      now_size+=1
      ate=0