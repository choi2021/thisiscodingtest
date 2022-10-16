import heapq

n,m,x=map(int,input().split())
INF=int(1e9)
graph=[[] for i in range(n+1)]
for i in range(m):
	a,b,c=map(int,input().split())
	graph[a].append((b,c))

def dijstra(start,end):
	q=[]
	distance=[INF]*(n+1)
	heapq.heappush(q,(0,start))
	distance[start]=0
	while q:
		dist,now=heapq.heappop(q)
		if dist>distance[now]:
			continue
		for i in graph[now]:
			cost=i[1]+dist
			if distance[i[0]]>cost:
				distance[i[0]]=cost
				heapq.heappush(q,(cost,i[0]))
	return distance[end]

result=0
for i in range(1,n+1):
	result=max(result,dijstra(i,x)+dijstra(x,i))

print(result)