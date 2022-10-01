# # 이동은 구현했는데 몸통의 움직임을 좌표로 나타내는데에서 막혓어..

# n=int(input())
# k=int(input())
# graph=[[0]*(n+1) for _ in range(n+1)]

# for i in range(k):
#     x,y=map(int,input().split())
#     graph[x][y]=1

# l=int(input())
# moves=[]
# for i in range(l):
#     sec,d=input().split()
#     moves.append((int(sec),d))


# dx=[0,-1,0,1]
# dy=[1,0,-1,0]

# d=0
# time=0
# body=[(1,1)]

# def turn_left(d):
#     if d+1==4:
#         return 0
#     return d+1

# def turn_right(d):
#     if d-1==0:
#         return 3
#     return d-1

# def solution():
#     global d,time,x,y
#     while True:
#         for move in moves:
#             sec,dir=move
#             for i in range(sec):
#                 x,y=body[0]
#                 nx=x+dx[d]
#                 ny=y+dy[d]
#                 for j in range(1,len(body)):
#                     nbx=x+dx[d]
#                     nby=y+dy[d]
#                     body[j]=(nbx,nby)
#                 if nx<1 or nx>n or ny<1 or ny>n and (nx,ny) in body:
#                     return time+1
#                 else:
#                     if graph[nx][ny]==1:
#                         body.append((x,y))   
#                     body[0]=(nx,ny)
#                     time+=1 
#             if dir=="L":
#                 d=turn_left(d)
#             elif dir=="D":
#                 d=turn_right(d)

# print(solution())

#책풀이:
n=int(input())
k=int(input())
data=[[0]*(n+1) for _ in range(n+1)]
info=[]

for _ in range(k):
    a,b=map(int,input().split())
    data[a][b]=1

l=int(input())
for _ in range(l):
    x,c=input().split()
    info.append((int(x),c))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(direction,c):
    if c=="L":
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4
    return direction

def simulate():
    x,y=1,1
    data[x][y]=2
    direction=0
    time=0
    index=0
    q=[(x,y)]
    while True:
        nx=x+dx[direction]
        ny=y+dy[direction]
        if 1<=nx<=n and 1<=ny<=n and data[nx][ny]!=2:
            if data[nx][ny]==0:
                data[nx][ny]=2
                q.append((nx,ny))
                px,py=q.pop(0)
                data[px][py]=0
            if data[nx][ny]==1:
                data[nx][ny]=2
                q.append((nx,ny))
            print(q)
        else:
            time+=1
            break
        x,y=nx,ny
        time+=1
        if index<l and time==info[index][0]:
            direction=turn(direction,info[index][1])
            index+=1
    return time

print(simulate())