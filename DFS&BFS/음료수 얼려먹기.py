from operator import truediv


n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

result=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]


def dfs(graph,start):
    x,y=start
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                dfs(graph,(nx,ny))

for i in range(n):
    for j in range(n):
        if graph[i][j]==0:
            result+=1
            graph[i][j]=1
            dfs(graph,(i,j))

print(result)


# 책풀이:

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result+=1