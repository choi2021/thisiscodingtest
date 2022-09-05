## 1. 그래프

그래프는 NODE(vertex)와 EDGE으로 표현된다. 표현방식에는 2가지가 존재한다: 인접행렬/인접리스트

1. 인접행렬
   2차원 배열에 각 노드가 연결된 형태를 기록하는 방식으로 2차원 리스트를 이용한다./
   연결되어 있지 않은 노드끼리는 무한의 비용이라고 작성한다

   필요없는 노드관계도 다 저장해, 노드 개수가 많을 수록 메모리가 낭비

```python
INF=99999999999
graph=[[0,7,5],[7,0,INF],[5,INF,0]]

print(graph)
```

2. 인접리스트
   리스트자료형을 이용해 기록하는 방식으로 연결된 노드 정보만 (노드,거리)로 전달한다.
   인접행렬에 비해 메모리가 효율적이지만, 특정 두 노드가 연결되어있는지 확인하는데 오래걸려
   따라서, 특정노드에 연결된 모든 인접 노드를 순회해야하는 경우
   인접 리스트 방식이 인접행렬보다 메모리 낭비가 적다.

```python
graph=[[] for _ in range(3)]

#노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

#노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)

```

## 2. DFS

DFS는 stack을 이용해 다음과 같은 로직으로 진행된다. 탐색에 O(N)이 걸린다.

1. 탐색 시작 노드를 스택에 넣고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접노드가 있으면 인접노드를 스택에 넣고 방문처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번을 더 이상 수행할 수 없을 때까지 반복한다.

위와 같은 방식을 구현하는데 재귀함수를 아래와 같이 구현할 수 있다.

```python
def dfs(graph,v,visited):
  visited[v]=True
  print(v,end=" ")
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited=[False]*9

dfs(graph,1,visited)
```

## BFS

BFS는 큐를 이용해 가까운 노드부터 탐색하는 알고리즘으로 다음과 같은 로직으로 진행된다. 탐색에 O(N)이 걸리지만 일반적으로 DFS보다 조금 더 빠르게 동작한다.

1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다.
3. 2번을 더이상 수행할 수 없을 때까지 반복한다.

위의 로직을 아래와 같이 구현할 수 있다.

```python
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
bfs(graph,1,visited)
```

추가적으로, 2차원 배열에서의 탐색문제를 만나면 그래프 형태로 바꿔서 생각해보자