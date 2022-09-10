
# import sys

# input=sys.stdin.readline
# INF=int(1e9)

# n,m =map(int,input().split())
# start=int(input())

# graph=[[] for i in range(n+1)]
# visited=[False]*(n+1)
# distance=[INF]*(n+1)

# for _ in range(m): 
#   a,b,c=map(int,input().split())
#   graph[a].append((b,c))

# def get_smallest_node(): 
#   min_value=INF
#   index=0
#   for i in range(n+1):
#     if distance[i]<min_value and not visited[i]:
#       min_value=distance[i]
#       index=i 
#   return index

# print(graph)

# def dijkstra(start):
#   distance[start]=0
#   visited[start]=True
#   for node in graph[start]:
#     distance[node[0]]=node[1] #처음 연결된 노드들의 거리 셋팅
#   for _ in range(n-1): #총 n-1개의 노드를 확인해야하니까
#     now=get_smallest_node() 
#     visited[now]=True
#     for j in graph[now]:
#       cost=distance[now]+j[1] #시작노드로 부터 거리+현재노드와의 거리
#       if cost<distance[j[0]]:
#         distance[j[0]]=cost

# dijkstra(start)

# for i in range(1,n+1):
#   if distance[i]==INF:
#     print("INFINITY")
#   else:
#     print(distance[i])

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())

graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start)) #큐에 시작점 셋팅
  distance[start]=0
  while q:
    dist, now=heapq.heappop(q) 
    if distance[now]<dist: #이미 처리했던 노드면 패스
      continue
    for node in graph[now]:
      cost=dist+ node[1]
      if cost <distance[node[0]]:
        distance[node[0]]=cost
        heapq.heappush(q,(cost,node[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i]==INF:
    print("INFINITY")
  else:
    print(distance[i])
