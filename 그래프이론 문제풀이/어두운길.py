# 내풀이: 최소의 비용으로 모두 연결되어있어야하므로 크루스칼 알고리즘 사용하자
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

n,m=map(int,input().split())
parent=[0]*n
edges=[]

for i in range(n):
  parent[i]=i

for i in range(m):
  x,y,cost=map(int,input().split())
  edges.append((cost,x,y))

edges.sort()
result=0

for edge in edges:
  cost,x,y=edge
  if find_parent(parent,x)!=find_parent(parent,y):
    union_parent(parent,x,y)
  else:
    result+=cost

print(result)

# 책풀이: 전체 가로등비용-최소 신장트리 비용으로 구했어

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
  

n,m=map(int,input().split())
parent=[0]*(n+1)

edges=[]
result=0

for i in range(1,n+1):
  parent[i]=i

for _ in range(m):
  x,y,z=map(int,input().split())
  edges.append((z,x,y))

edges.sort()
total=0

for edge in edges:
  cost,a,b=edge
  total+=cost
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost

print(total-cost)