from collections import deque
n=int(input())
a,b=map(int,input().split())
m=int(input())
graph=[[] for i in range(n+1)]
for _ in range(m):
	x,y=map(int,input().split())
	graph[x].append(y)
	graph[y].append(x)
INF=int(1e9)
distance=[INF]*(n+1)

# def bfs(start):
# 	distance[start]=0
# 	q=deque([(0,start)])
# 	while q:
# 		dist,node=q.popleft()
# 		for i in graph[node]:
# 			if distance[i]==INF:
# 				q.append((dist+1,i))
# 				distance[i]=dist+1
# bfs(a)
# if distance[b]==INF:
# 	print(-1)
# else:
# 	print(distance[b])

# def dfs(node,num):
# 	distance[node]=num
# 	for i in graph[node]:
# 		if distance[i]==INF:
# 			dfs(i,num+1)
#
# dfs(a,0)
# print(distance)