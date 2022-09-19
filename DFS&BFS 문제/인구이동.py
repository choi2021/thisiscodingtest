# # 내풀이: DFS/BFS의 전형적인 문제지만, 아직 탐색하는 알고리즘이 부족해..
# # 1. 각 나라마다 돌면서 상하좌우로 가능한 연합 찾기
# # 2. 연합가능한 나라끼리 묶어주기
# # 
# n,l,r=map(int,input().split())
# graph=[]
# for i in range(n):
#   graph.append(list(map(int,input().split())))

# unions=[[False]*n for i in range(n)]

# dx=[1,-1,0,0]
# dy=[0,0,1,-1]

# def dfs(x,y):
#   for i in range(4):
#     nx=x+dx[i]
#     ny=y+dy[i]
#     if 0<=nx<n and 0<ny<n:
#       if l<=abs(graph[x][y]-graph[nx][ny])<=r and unions[x][y]==False:    
#         unions[x][y]=True
#         dfs(nx,ny)
#         return True
#   return False

# def combine_nations():
#   nations=[]
#   for i in range(n):
#     for j in range(n):
#       if unions[i][j]==True:
#         nations.append((i,j))
#   if len(nations)==0:
#     return False
#   popularity=0
#   for x,y in nations:
#     popularity+=graph[x][y]//len(nations)
#   for x,y in nations:
#     graph[x][y]=popularity
#   return True

# result=0
# while possible==True:
#   for i in range(n):
#     for j in range(n):
#       d
#   if combine_nations()==False:
#     break
#   result+=1
# print(result)


# 책풀이: DFS이용해서 탐색, 연합가능한걸 묶는 방식에서 차이를 보여
from collections import deque

n,l,r=map(int,input().split())

graph=[]
for _ in range(n):
  graph.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

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

print(total_count)