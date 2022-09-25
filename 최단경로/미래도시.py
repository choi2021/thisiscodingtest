# 내풀이: A->K->M: 플루이드 워셜 알고리즘 쓸 수 있지 않을까
# n,m이 100이하니까 n^3해도 100만 정도
INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

for i in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

x,k=map(int,input().split())


for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

if graph[1][k]+graph[k][x]>=INF:
  print(-1)
else:
  print(graph[1][k]+graph[k][x])


#책풀이:
INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

for _ in range(m):
  a,b= map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1


x,k=map(int,input().split())

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

distance=graph[1][k]+[k][x]

if distance>=INF:
  print("-1")
else:
  print(distance)