# 플로이드 워셜
# INF=int(1e9)
# import sys
# input=sys.stdin.readline
# v,e=map(int,input().split())
#
# distance=[[INF]*(v+1) for i in range(v+1)]
# for i in range(e):
# 	a,b,c=map(int,input().split())
# 	distance[a][b]=c
#
# for k in range(1,v+1):
# 	for i in range(1,v+1):
# 		for j in range(1,v+1):
# 			distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
#
# result=INF
# for i in range(1,v+1):
# 	result=min(result,distance[i][i])
# if result>=INF:
# 	print(-1)
# else:
# 	print(result)

#다익스트라

import heapq
INF=int(1e9)
v,e = map(int, input().split())
graph = [[] for _ in range(v+1)]
distance = [[INF] * (v+1) for _ in range(v+1)]

q=[]
result=INF
for _ in range(e):
	a,b,c=map(int,input().split())
	graph[a].append((b,c))
	distance[a][b]=c
	heapq.heappush(q,(c,a,b))

while q:
	dist,start,end=heapq.heappop(q)
	if start==end:
		result=dist
		break
	if dist>distance[start][end]:
		continue
	for i in graph[end]:
		cost=dist+i[1]
		if cost<distance[start][i[0]]:
			distance[start][i[1]]=cost
			heapq.heappush(q,(cost,start,i[0]))

print(result)