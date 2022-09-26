#내풀이: DFS로 풀어보려했지만 실패..
# DFS를 이용하려면 간선의 비용이 같아야하는데 잘못사용했어.
# from collections import deque

# # t=int(input())
# # for i in range(t):
# n=int(input())
# graph=[]
# visited=[[False]*n for i in range(n)]

# for i in range(n):
#     graph.append(list(map(int,input().split())))

# dx=[1,-1,0,0]
# dy=[0,0,1,-1]

# start=(0,0)

# def bfs(x,y):
#     q=deque()
#     temp=graph[:]
#     q.append((x,y))
#     visited[x][y]=True
#     while q:
#       x,y=q.popleft()
#       for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if nx<0 or ny<0 or nx>=n or ny>=n:
#           continue
#         if visited[nx][ny]==False:
#           graph[nx][ny]+=graph[x][y]
#           q.append((nx,ny))
#           visited[nx][ny]=True
#         # else:
#         #   total=temp[nx][ny]+graph[x][y]
#         #   if total<graph[nx][ny]:
#         #     graph[nx][ny]=total
#         #     q.append((nx,ny))
#     return graph[n-1][n-1]

# print(bfs(0,0))
# print(graph)

# 책풀이:
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

for tc in range(int(input())):
  n=int(input())
  graph=[]
  for i in range(n):
    graph.append(list(map(int,input().split())))
  
  distance=[[INF]*n for _ in range(n)]

  x,y=0,0

  q=[(graph[x][y],x,y)]
  distance[x][y]=graph[x][y]

  while q:
    dist,x,y=heapq.heappop(q)
    if distance[x][y]<dist:
      continue
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or 0>ny or ny>=n:
        continue
      cost=dist+graph[nx][ny]
      if cost<distance[nx][ny]:
        distance[nx][ny]=cost
        heapq.heappush(q,(cost,nx,ny))

  print(distance[n-1][n-1])



