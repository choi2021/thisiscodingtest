# 내풀이: 모든 지점에서의 모든 지점으로의 최단거리를 계산해야 하므로 플로이드 워셜
# 노선이 하나가 아닐 수도 있기 때문에 최소를 처음 할당해줘
INF=int(1e9)
n=int(input())
m=int(input())
graph=[[INF]*(n+1) for i in range(n+1)]



for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0


for _ in range(m):
  start,dest,cost=map(int,input().split())
  if graph[start][dest]!=INF:
      graph[start][dest]=min( graph[start][dest],cost)
      continue
  graph[start][dest]=cost

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j]==INF:
      print(0, end=" ")
      continue
    print(graph[i][j], end=" ")
  print()

