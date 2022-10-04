#내풀이: n=3000000 m=1000000

from collections import deque
import sys

input=sys.stdin.readline
INF=int(1e9)
n,m,k,start=map(int,input().split())
graph=[[] for i in range(n+1)]

for _ in range(m):
  st,dist=map(int,input().split())
  graph[st].append(dist)

dist=[INF]*(n+1)

def bfs(start):
  q=deque([start])
  dist[start]=0
  while q:
    now=q.popleft()
    for j in graph[now]:
      if dist[j]==INF:
        dist[j]=dist[now]+1
        q.append(j)



result=[]
bfs(start)
result=False
for i in range(1,n+1):
  if dist[i]==k:
    result=True
    print(i)

if result==False:
  print(-1)