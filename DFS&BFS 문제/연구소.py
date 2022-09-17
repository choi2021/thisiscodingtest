# # BFS를 이용해보자
# # N,M이 범위가 3~8이므로 완전탐색써도 될듯
# # 1. 벽을 세개 세울 수 있는 모든 경우의수의 graph로 만들어서
# # 2. 바이러스 지점부터 돌아가면서 0이면 2로 다바꿔
# # 3. 0인 지점을 세서 최댓값을 찾아줘

# from itertools import combinations


# N,M=map(int,input().split())
# graph=[]

# for _ in range(N):
#   graph.append(list(map(int,input().split())))

# vacant_spaces=[]
# viruses=[]

# treated_graphes=[]

# dx=[1,-1,0,0]
# dy=[0,0,1,-1]

# def bfs(x,y,graph):
#   stack=[(x,y)]
#   while stack:
#     x,y=stack.pop()
#     for i in range(4):
#       nx=x+dx[i]
#       ny=y+dy[i]
#       if nx<0 or ny<0 or nx>=N or ny>=M:
#         continue
#       elif graph[nx][ny]==1 or graph[nx][ny]==2:
#         continue
#       elif graph[nx][ny]==0:
#         graph[nx][ny]=2
#         stack.append((nx,ny))
#   return graph
    

# for i in range(N):
#   for j in range(M):
#     if graph[i][j]==0:
#       vacant_spaces.append((i,j))
#     elif graph[i][j]==2:
#       viruses.append((i,j))

# result=[]
# for case in list(combinations(vacant_spaces,3)):
#   treated_graph=graph[:]
#   for i in range(3):
#     x,y=case[i]
#     treated_graph[x][y]=1
#   for virus in viruses:
#     x,y=virus
#     treated_graph=bfs(x,y,treated_graph)

#   count=0
#   for i in range(N):
#     for j in range(j):
#       if treated_graph[i][j]==0:
#         count+=1
#   result.append(count)

# print(max(result))

# 책풀이

n,m=map(int,input().split())
data=[]
temp=[[0]*m for _ in range(n)]

for _ in range(n):
  data.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

result=0

def virus(x,y):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx>=0 and nx<n and ny>=0 and ny<m:
      if temp[nx][ny]==0:
        temp[nx][ny]=2
        virus(nx,ny)

def get_score():
  score=0
  for i in range(n):
    for j in range(m):
      if temp[i][j]==0:
        score+=1
  return score

def dfs(count):
  global result
  if count==3:
    for i in range(n):
      for j in range(m):
        temp[i][j]=data[i][j]
    for i in range(n):
      for j in range(m):
        if temp[i][j]==2:
          virus(i,j)
    result=max(result,get_score())
    return
  for i in range(n):
    for j in range(m):
      if data[i][j]==0:
        data[i][j]=1
        count+=1
        dfs(count)
        data[i][j]=0
        count-=1
dfs(0)
print(result)
  