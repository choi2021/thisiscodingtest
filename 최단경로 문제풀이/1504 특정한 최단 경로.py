import heapq,sys

input=sys.stdin.readline

n,e=map(int,input().split())
graph=[[]for i in range(n+1)]
INF=int(1e9)

for i in range(e):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

v1,v2=map(int,input().split())

def dijkstra(start,end):
  distance=[INF]*(n+1)
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if dist>distance[now]:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))
  return distance[end]

result=INF
result=min(dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n),result)
result=min(dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n),result)
if result<INF:
  print(result)
else:
  print(-1)