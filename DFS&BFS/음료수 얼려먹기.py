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

