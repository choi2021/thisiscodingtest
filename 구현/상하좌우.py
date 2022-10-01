n=int(input())
data=input().split()
x,y=(1,1)

for i in range(len(data)):
  if data[i]=="R":
    nx=x
    ny=y+1
  elif data[i]=="U":
    nx=x-1
    ny=y
  elif data[i]=="D":
    nx=x+1
    ny=y
  else:
    nx=x
    ny=y-1

  if 0<nx<=n and 0<ny<=n:
    x=nx
    y=ny  

print(x,y)

#책풀이:
n=int(input())
x,y=1,1
plans=input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=["L","R","U","D"]

for plan in plans:
  for i in range(len(move_types)):
    if plan==move_types[i]:
      nx=x+dx[i]
      ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
      continue
    x,y=nx,ny

print(x,y)