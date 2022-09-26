#내풀이: 그래프문제로 특정 지점부터 다른 모든 지점으로 가는데 걸리는 시간이 필요하니까 다익스트라 알고리즘을 이용
# n<=30000, m<200000일때이므로 O(nlogn)사용해도 괜찮아

import heapq

INF=int(1e9)
n,m,c=map(int,input().split())
graph=[[]for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
  x,y,z=map(int,input().split())
  graph[x].append((y,z))

def dijstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))


dijstra(c)
max_time=0
num=0
for i in range(n):
  if distance[i]!=INF:
    if max_time<distance[i]:
      max_time=distance[i]
    num+=1

print(num,max_time)


# 책풀이

import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m,start=map(int,input().split())

graph=[[]for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
  x,y,z=map(int,input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)
count=0
max_distance=0
for d in distance:
  if d!=INF:
    count+=1
    max_distance=max(max_distance,d)

print(count-1,max_distance)