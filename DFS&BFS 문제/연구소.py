# 1. 벽을 세우기위해서 백트래킹을 사용해
# 2. 벽을 세우고 바이러스를 퍼뜨려
# 3. 결과중 최댓값을 구해

n,m=map(int,input().split())
graph=[]

temp=[[0]*n for _ in range(n)]
for _ in range(n):
  graph.append(list(map(int,input().split())))

dx=[1,0,-1,0]
dy=[0,1,0,-1]

result=-1
num=0

def spread(x,y):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<n and 0<=ny<n:
      if temp[nx][ny]==0:
        temp[nx][ny]=2
        spread(nx,ny)

def get_score():
  score=0
  for i in range(n):
    for j in range(n):
      if temp[i][j]==0:
        score+=1
  return score

def dfs(count):
  global result
  if count==3:
    for i in range(n):
      for j in range(n):
        temp[i][j]=graph[i][j]
    for i in range(n):
      for j in range(n):
        if temp[i][j]==2:
          spread(i,j)
    result=max(result,get_score())
    return 

  for i in range(n):
    for j in range(n):
      if graph[i][j]==0:
        graph[i][j]=1
        count+=1
        dfs(count)
        count-=1
        graph[i][j]=0


dfs(0)
print(result)
