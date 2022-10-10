from collections import deque

n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]

for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs_visited=[False]*(n+1)
bfs_visited=[False]*(n+1)


def dfs(node):
  dfs_visited[node]=True
  print(node, end=" ")
  graph[node].sort()
  for next_node in graph[node]:
    if dfs_visited[next_node] ==False:
      dfs(next_node)

def bfs(start):
  q=deque([start])
  bfs_visited[start]=True
  while q:
    now=q.popleft()
    print(now,end=" ")
    graph[now].sort()
    for next_node in graph[now]:
      if bfs_visited[next_node]==False:
        q.append(next_node)
        bfs_visited[next_node]=True


dfs(v)
print()
bfs(v)