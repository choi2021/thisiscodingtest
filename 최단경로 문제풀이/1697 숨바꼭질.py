# import heapq

# n,k=map(int,input().split())
# visited=[False]*100001

# visited[n]=True
# q=[]
# heapq.heappush(q,(0,n))

# while q:
#   dist,pos=heapq.heappop(q)
#   if pos==k:
#     print(dist)
#     break
#   if pos*2<len(visited) and not visited[pos*2]:
#     visited[pos*2]=True
#     heapq.heappush(q,(dist+1,pos*2))
#   for i in (pos+1,pos-1):
#     if 0<=i<len(visited) and not visited[i]:
#       visited[i]=True
#       heapq.heappush(q,(dist+1,i))

import heapq

n,k=map(int,input().split())
INF=int(1e9)

time=[INF]*(100001)

q=[]
time[n]=0
heapq.heappush(q,(0,n))
while q:
  now,pos=heapq.heappop(q)
  if pos==k:
    print(now)
    break
  if now>time[pos]:
    continue
  if pos*2<100001 and time[pos*2]>now+1:
    time[pos*2]=now+1
    heapq.heappush(q,(now+1,pos*2))
  if pos+1<100001 and time[pos+1]>now+1:
    time[pos+1]=now+1
    heapq.heappush(q,(now+1,pos+1))
  if pos-1>=0 and time[pos-1]>now+1:
    time[pos-1]=now+1
    heapq.heappush(q,(now+1,pos-1))

  
