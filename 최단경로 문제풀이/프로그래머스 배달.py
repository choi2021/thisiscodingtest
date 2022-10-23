n=5
road=[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
k=3

import heapq

def solution(n, road, k):
	INF=int(1e9)
	graph=[[] for i in range(n+1)]
	for i in road:
		a,b,c=i
		graph[a].append((b,c))
		graph[b].append((a,c))
	distance=[INF]*(n+1)

	q = [(0, 1)]
	distance[1] = 0
	while q:
		dist, now = heapq.heappop(q)
		if dist > distance[now]:
			continue
		for i in graph[now]:
			cost=dist+i[1]
			if cost<distance[i[0]]:
				distance[i[0]]=cost
				heapq.heappush(q,(cost,i[0]))
	return len(list(filter(lambda x:x<=k,distance)))
solution(n,road,k)