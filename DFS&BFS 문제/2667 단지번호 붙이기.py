# 1. DFS로 모든 좌표를 돌면서 이어져있는 단지를 찾아
# 2. graph에서 1이면 dfs함수를 실행해
# 3. dfs는 받은 좌표와 num을 이용해서 이어진 단지를 num으로 표기하고, graph는 0으로 표기해
# 4. 갯수를 세고

n=int(input())
graph=[]
new_graph=[[0]*n for _ in range(n)]

for i in range(n):
  graph.append(list(map(int,input())))


dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y,num):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<n and 0<=ny<n:
      if graph[nx][ny]==1:
        new_graph[nx][ny]=num
        graph[nx][ny]=0
        dfs(nx,ny,num)

num=0

for i in range(n):
  for j in range(n):
    if graph[i][j]==1:
      graph[i][j]=0
      num+=1
      new_graph[i][j]=num
      dfs(i,j,num)


answer=[0]*(num+1)
for i in range(1,num+1):
  count=0
  for row in new_graph:
    count+=row.count(i)
  answer[i]=count

print(num)
answer.sort()
for i in range(1,num+1):
  print(answer[i])


