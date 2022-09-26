n,m=map(int,input().split())
parent=[0]*(n+1)

def find_parent(parent,a):
  if parent[a]!=a:
    parent[a]=find_parent(parent,parent[a])
  return parent[a]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

for i in range(n+1):
  parent[i]=i

for i in range(m):
  k,a,b=map(int,input().split())
  if k==1:
    if parent[a]==parent[b]:
      print("YES")
    else:
      print("NO")
  else:
    union_parent(parent,a,b)
    