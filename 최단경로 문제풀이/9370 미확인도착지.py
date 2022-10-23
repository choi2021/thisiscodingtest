import heapq
import sys
input=sys.stdin.readline

def dijstra(start):
	distance = [INF] * (2001)
	q=[]
	distance[start]=0
	heapq.heappush(q,(0,start))
	while q:
		dist,now=heapq.heappop(q)
		if dist>distance[now]:
			continue
		for i in graph[now]:
			cost=dist+i[1]
			if cost<distance[i[0]]:
				distance[i[0]]=cost
				heapq.heappush(q,(cost,i[0]))
	return distance

Test=int(input())

for _ in range(Test):
	INF = int(1e9)
	n, m, t = map(int, input().split())
	s, g, h = map(int, input().split())
	graph = [[] for i in range(n + 1)]
	dests = []

	middle = INF

	for i in range(m):
		a, b, d = map(int, input().split())
		graph[a].append((b, d))
		graph[b].append((a, d))

	for i in range(t):
		dests.append(int(input()))
	dests.sort()
	start_dist=dijstra(s)
	g_dist=dijstra(g)
	h_dist=dijstra(h)
	for des in dests:
		if start_dist[des]== (start_dist[g] + g_dist[h]+ h_dist[des]) or start_dist[des] == (
			start_dist[h] + g_dist[h] + g_dist[des]):
			print(des, end=" ")

