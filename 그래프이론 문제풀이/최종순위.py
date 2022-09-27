# #내풀이: graph[a][b]는 a가 b보다 순위가 낮다는 의미로 만든뒤 순위조정이 있으면 좌표의 값만 바꾸어준다.
# n=int(input())
# prev_order=list(map(int,input().split()))
# m=int(input())
# graph=[[0]*(n+1) for i in range(n+1)]

# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if prev_order[i-1]>prev_order[j-1]:
#       graph[i][j]=1

# for i in range(m):
#   a,b=map(int,input().split())
#   graph[a][b]=0
#   graph[b][a]=1

# def check_Result(graph):
#   result=[0]*n
#   counts=[0]*n
#   for i in range(1,n+1):
#     num=graph[i].count(1)
#     counts[num]+=1
#     result[i-1]=num+1

#   for num in counts:
#     if num>=2:
#       return "IMPOSSIBLE"
  
#   for i in result:
#     print(i, end=" ")
#   return None

# if check_Result(graph)!=None:
#   print( check_Result(graph))

# 책풀이: 위상정렬을 이용한 풀이

from collections import deque
from pickletools import read_unicodestring1

for tc in range(int(input())):
  n=int(input())
  indegree=[0]*(n+1)
  graph=[[False]*(n+1) for i in range(n+1)]
  data=list(map(int,input().split()))
  for i in range(n):
    for j in range(i+1,n):
      graph[data[i]][data[j]]=True
      indegree[data[j]]+=1

  m=int(input())
  for i in range(m):
    a,b=map(int,input().split())
    if graph[a][b]:
      graph[a][b]=False
      graph[b][a]=True
      indegree[a]+=1
      indegree[b]-=1
    else:
      graph[a][b]=True
      graph[b][a]=False
      indegree[a]-=1
      indegree[b]+=1
  result=[]
  q=deque()

  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)
  certain=True
  cycle=False

  for i in range(n):
    if len(q)==0:
      cycle=True
      break
    if len(q)>=2:
      certain=False
      break
    now=q.popleft()
    result.append(now)
    for j in range(1,n+1):
      if graph[now][j]:
        indegree[j]-=1
        if indegree[j]==0:
          q.append(j)

  if cycle:
    print("IMPOSSIBLE")
  elif not certain:
    print("?")
  else:
    for i in result:
      print(i,end=" ")
    print()
  