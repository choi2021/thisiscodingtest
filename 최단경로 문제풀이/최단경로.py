import heapq
import sys

INF=int(1e9)
input=sys.stdin.readline
n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for next_node,d in graph[now]:
            new_distance=d+dist
            if new_distance<distance[next_node]:
                distance[next_node]=new_distance
                heapq.heappush(q,(new_distance,next_node))
dijstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])


