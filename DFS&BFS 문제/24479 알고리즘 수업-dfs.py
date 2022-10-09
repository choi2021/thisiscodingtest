import sys

sys.setrecursionlimit(1000000 )
input=sys.stdin.readline
n,m,r=map(int,input().split())
graph=[[] for i in range(n+1)]
visited=[0]*(n+1)

for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

order=1;
def dfs(graph,start):
  global order
  visited[start]=order
  graph[start].sort()
  for node in graph[start]:
    if visited[node]==0:
      order+=1
      dfs(graph,node)

dfs(graph,r)

for i in range(1,n+1):
  print(visited[i])