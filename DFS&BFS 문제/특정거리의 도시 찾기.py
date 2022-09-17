from collections import deque

N,M,K,X=map(int,input().split())
graph=[[] for _ in range(N+1)]

for _ in range(M):
  a,b=map(int,input().split())
  graph[a].append(b)

INF=1e+9
dist=[INF]*(N+1)

q=deque([X])
dist[X]=0

while q:
  node=q.popleft()
  for dest in graph[node]:
    if dist[dest]==INF:
      q.append(dest)
      dist[dest]=dist[node]+1

check=False
for i in range(1,N+1):
  if dist[i]==K:
    check=True
    print(i)
if check==False:
  print(False)

#책풀이
#모든 도로의 거리가 1이므로 너비우선탐색(BFS)를 이용할 수 있다.

# from collections import deque:
# n,m,k,x=map(int,input().split())
# graph=[[] for _ in range(n+1)]

# for _ in range(m):
#   a,b=map(int,input().split())
#   graph[a].append(b)

# distance=[-1]*(n+1)
# distance[x]=0

# q=deque([x])
# while q:
#   now=q.popleft()
#   for next_node in graph[now]:
#     if distance[next_node]==-1:
#       distance[next_node]=distance[now]+1
#       q.append(next_node)

# check=False
# for i in range(1,dist):
#   if dist[i]==K:
#     check=True
#     print(i)
# if check==False:
#   print(False)