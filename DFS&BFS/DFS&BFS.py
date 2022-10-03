def dfs(graph,v,visited):
  visited[v]=True
  print(v, end=" ")
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

from collections import deque
def bjs(graph,start,visited):
  queue=deque([start])
  visited[start]=True
  while queue:
    v=queue.popleft()
    print(v, end=" ")
    for i in graph[v]:
      if i not in visited:
        queue.append(i)
        visited[i]=True

  