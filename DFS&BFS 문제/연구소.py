import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
temp=[[0]*m for i in range(n)]

for _ in range(n):
  graph.append(list(map(int,input().split())))

dx=[1,0,-1,0]
dy=[0,1,0,-1]
result=0

def get_score():
  count=0
  for i in range(n):
    for j in range(m):
      if temp[i][j]==0:
        count+=1
  return count

def spread(x,y):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0>nx or n<=nx or 0>ny or m<=ny:
      continue
    if 0<=nx<n and 0<=ny<m:
      if temp[nx][ny]==0:
        temp[nx][ny]=2
        spread(nx,ny)

def dfs(num):
  global result
  if num==3:
    for i in range(n):
      for j in range(m):
        temp[i][j]=graph[i][j] 
    for i in range(n):
      for j in range(m):
        if temp[i][j]==2:
          spread(i,j)
    result=max(result,get_score())
    return 

  for i in range(n):
    for j in range(m):
      if graph[i][j]==0:
        graph[i][j]=1
        num+=1
        dfs(num)
        num-=1
        graph[i][j]=0

dfs(0)
print(result)