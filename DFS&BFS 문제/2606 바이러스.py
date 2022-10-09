from collections import deque

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited=[False]*(n+1)
result=0
def bfs(start):
  global result
  q=deque([start])
  visited[start]=True
  while q:
    now=q.popleft()
    for i in graph[now]:
      if visited[i]==False:
        result+=1
        q.append(i)
        visited[i]=True



def dfs(node):
  global result
  visited[node]=True
  print(visited)
  for i in graph[node]:
    if visited[i]==False:
      result+=1
      dfs(i)

dfs(1)
print(result)