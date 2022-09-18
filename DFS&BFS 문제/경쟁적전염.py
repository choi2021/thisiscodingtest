# # 내 풀이: DFS를 이용하고 
# # 1.매초마다 상.하.좌.우 순으로 하나 증식
# # 2. 순서는 숫자가 낮은 바이러스 부터
# # 3. 각 바이러스 위치를 저장하고 숫자가 낮은 바이러스부터 
# # 4. 내가 생각했던건 숫자가 낮은 바이러스에서 모든 방향에서 가능한게 아니라 1초당 상하좌우순서에 맞게 하나씩 증가하는줄...




N,K=map(int,input().split())

graph=[]
viruses=[]
temp=[]

for i in range(N):
  graph.append(list(map(int,input().split())))
  for j in range(N):
    if graph[i][j]!=0 and (i,j):
      viruses.append((i,j,graph[i][j]))



S,X,Y=map(int,input().split())


dx=[0,0,-1,1]
dy=[-1,1,0,0]

viruses=sorted(viruses,key=lambda x:x[2])

def dfs(x,y,virus):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or nx>=N or ny<0 or ny>=N:
      continue
    if graph[nx][ny]==0:
      graph[nx][ny]=virus  
      temp.append((nx,ny,virus))
  return False

num=0
while num<S:
  temp=[]
  for virus in viruses:
    x,y,k=virus
    dfs(x,y,k)
  viruses=temp
  viruses=sorted(viruses,key=lambda x:x[2])
  num+=1

print(graph[X-1][Y-1])

# # BFS를 이용해서 낮은 번호부터 넣어서 풀이
# # 바이러스의 종류,시간, x,y를 함께 큐에 넣어
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

dx=[0,0,-1,1]
dy=[-1,1,0,0]

while q:
  virus,s,x,y=q.popleft()
  if s==target_s:
    break
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx and nx<n and 0<=ny and ny<n:
      if graph[nx][ny]==0:
        graph[nx][ny]=virus
        q.append((virus,s+1,nx,ny))

print(graph[target_x-1][target_y-1])