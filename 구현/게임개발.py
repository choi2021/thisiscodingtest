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

#책풀이:
n,m=map(int,input().split())
d=[[0]*m for i in range(n)]
x,y,direction=map(int,input().split())
d[x][y]=1

array=[]
for i in range(n):
  array.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
  global direction
  direction-=1
  if direction==-1:
    direction=3

count=1
turn_time=0
while True:
  turn_left()
  nx=x+dx[direction]
  ny=y+dy[direction]
  if d[nx][ny]==0 and array[nx][ny]==0:
    d[nx][ny]=1
    x,y=nx,ny
    count+=1
    turn_time=0
    continue
  else:
    turn_time+=1

  if turn_time==4:
    nx=x-dx[direction]
    ny=y-dy[direction]
    if array[nx][ny]==0:
      x,y=nx,ny
    else:
      break
    turn_time=0

print(count)