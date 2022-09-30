n,m=map(int,input().split())
x,y,d=map(int,input().split())

graph=[]

for i in range(n):
  graph.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def find_direction(d):
  if d-1<0:
    return 3
  return d-1

result=1

data=[]
while True:
  find=False
  graph[x][y]=1
  for _ in range(4):
      d=find_direction(d)
      nx=x+dx[d]
      ny=y+dy[d]
      if graph[nx][ny]==0 and 0<=nx<n and 0<=ny<n:
        result+=1
        x,y=nx,ny
        find=True
        break
    
  if find==True:
    continue
  nx=x+dx[(d+2)%4]
  ny=y+dy[(d+2)%4]
  if graph[nx][ny]==1:
    break
  x,y=nx,ny

print(result)  
print(data)  
