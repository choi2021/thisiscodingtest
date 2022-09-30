from turtle import pos


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
    print(i)
    x=nx
    y=ny  

print(x,y)