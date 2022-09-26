from collections import deque

n=int(input())
indegree=[0]*(n+1)
times=[0]*(n+1)
graph=[[] for i in range(n+1)]
result=[0]*(n+1)

for i in range(1,n+1):
  data=list(map(int,input().split()))
  for j in range (len(data)-1):
    if j==0:
      times[i]=data[j]
    else:
      graph[data[j]].append(i)
      indegree[i]+=1

def topology_sort():
  q=deque()
  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)
      result[i]=times[i]
  while q:
    now=q.popleft()
    for i in graph[now]:
      indegree[i]-=1
      if result[now]>result[i]:
        result[i]=result[now]
      if indegree[i]==0:
        q.append(i)
        result[i]+=times[i]

topology_sort()
print(result)


#책풀이:

from collections import deque
import copy

n=int(input())
indegree=[0]*(n+1)
graph=[[]for i in range(n+1)]
time=[0]*(n+1)

for i in range(1,n+1):
  data=list(map(int,input().split()))
  time[i]=data[0]
  for x in data[1:-1]:
    indegree[i]+=1
    graph[x].append(i)


def topology_sort():
  result=copy.deepcopy(time)
  q=deque()

  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    for i in graph[now]:
      result[i]=max(result[i],result[now]+time[i])
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)
        
  for i in range(1,n+1):
    print(result[i])