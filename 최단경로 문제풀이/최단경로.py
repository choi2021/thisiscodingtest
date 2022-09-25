import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

v,e=map(int,input().split())
k=int(input())
graph=[[] for i in range(v+1)]
distance=[INF]*(v+1)

for i in range(e):
  u,v,w=map(int,input().split())
  graph[u].append((v,w))


def dijstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for v,w in graph[now]:
      cost=dist+w
      if cost<distance[v]:
        distance[v]=cost
        heapq.heappush(q,(cost,v))

dijstra(k)

for i in range(1,v+1):
  if distance[i]==INF:
    print("INF")
  else:
    print(distance[i])