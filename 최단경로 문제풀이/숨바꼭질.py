import heapq

INF=int(1e9)
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)


for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dijstra(start):
  distance[start]=0
  q=[]
  heapq.heappush(q,(0,start))
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for node in graph[now]:
      cost=1+dist
      if cost<distance[node]:
        distance[node]=cost
        heapq.heappush(q,(cost,node))

dijstra(1)
max_distance=0
for i in distance:
  if i==INF:
    continue
  else:
    if i>max_distance:
      max_distance=i 

print(distance.index(max_distance),max_distance,distance.count(max_distance))