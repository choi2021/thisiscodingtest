#1. 인접행렬=2차원 배열을 이용해서 작성

INF=99999999999
graph=[[0,7,5],[7,0,INF],[5,INF,0]]

print(graph)


#2. 인접리스트=리스트를 이용해서 작성

graph=[[] for _ in range(3)]

#노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

#노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)


# DFS (Depth-First Search)는 깊이 우선 탐색이라 부르며 깊은 부분을 우선적으로 탐색한다.

def dfs(graph,v,visited):
  visited[v]=True
  print(v,end=" ")
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)



#BFS (Breadth First Search) 는 너비 우선 탐색이라 부르며 가까운 노드부터 탐색하는 알고리즘이다.

from collections import deque

def bfs(graph,start,visited):
  queue=deque([start])
  visited[start]=True
  while queue:
    v=queue.popleft()
    print(v,end=" ")
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited=[False]*9

dfs(graph,1,visited)
bfs(graph,1,visited)