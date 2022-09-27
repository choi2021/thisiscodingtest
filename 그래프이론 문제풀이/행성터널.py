# # 서로 연결되어야하고, 최소비용을 물어보니까 크루스칼 알고리즘을 쓸거야
# # 1. edge끼리의 비용을 구해야해 전체를 다 확인해야하니까 메모리초과...
# 왜 인접한 행성끼리만 계산하면 되는지 아직 이해가안돼

# from itertools import combinations
# import sys

# from macpath import split
# input=sys.stdin.readline
# def find_parent(parent,x):
#   if parent[x]!=x:
#     parent[x]=find_parent(parent,parent[x])
#   return parent[x]

# def union_parent(parent,a,b):
#   a=find_parent(parent,a)
#   b=find_parent(parent,b)
#   if a<b:
#     parent[b]=a
#   else:
#     parent[a]=b

# n=int(input())
# edges=[]
# graph=[]
# parent=[0]*n

# for i in range(n):
#   parent[i]=i

# for i in range(n):
#   x,y,z=map(int,input().split())
#   graph.append((x,y,z))

# for i,j in list(combinations(range(n),2)):
#   x1,y1,z1=graph[i]
#   x2,y2,z2=graph[j]
#   dist=min(abs(x1-x2),abs(y1-y2),abs(z1-z2))
#   if len(edges)>=3*n:
#     max_value=max(edges,key=x:x[0])
#     max_index=edges.index(max_value)
#     edges[max]


# edges.sort()
# result=0
# for edge in edges:
#   cost,a,b=edge
#   if find_parent(parent,a)!=find_parent(parent,b):
#     union_parent(parent,a,b)
#     result+=cost
# print(result)

#책풀이: 3가지 축을 다 동시에 생각하지 않고 각 축에 따른 거리로 크루스칼을 진행해

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n=int(input())
parent=[0]*(n+1)

edges=[]
result=0

for i in range(1,n+1):
  parent[i]=i

x=[]
y=[]
z=[]

for i in range(1,n+1):
  data=list(map(int,input().split()))
  x.append((data[0],i))
  y.append((data[1],i))
  z.append((data[2],i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
  edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
  edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
  edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))


edges.sort()

for edge in edges:
  cost, a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost


print(result)