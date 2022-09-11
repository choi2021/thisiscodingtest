#내풀이: 다익스트라를 두번해서 구한 다음에 최소거리를 더 하려 했어

# import heapq
# import sys
# input=sys.stdin.readline
# INF=int(1e9)
# N, M=map(int,input().split())
# graph=[[] for _ in range(N+1)]


# for i in range(M):
#   a,b=map(int,input().split())
#   graph[a].append(b)
#   graph[b].append(a)

# X,K=map(int,input().split())

# def dijkstara(start,end):
#   distance=[INF]*(N+1)
#   q=[]
#   heapq.heappush(q,(0,start))
#   distance[start]=0
#   while q:
#     dist,now=heapq.heappop(q)
#     if distance[now]<dist:
#       continue
#     for i in graph[now]:
#       cost=dist+1
#       if cost<distance[i]:
#         distance[i]=cost
#         heapq.heappush(q,(cost,i))
#   return distance[end]

# print(dijkstara(1,K)+dijkstara(K,X))

#풀이:플로이드 워셜 알고리즘

import sys

INF=int(1e9)
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[INF]*(N+1) for _ in range(N+1)]

for a in range(1,N+1):
  for b in range(1,N+1):
    if a==b:
      graph[a][b]=0

for i in range(M):
  a,b=map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

X,K=map(int,input().split())

for k in range(1,N+1):
  for a in range(1,N+1):
    for b in range(1,N+1):
        graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

distance=graph[1][K]+graph[K][X]
if distance>=INF:
  print("-1")
else:
  print(distance)




