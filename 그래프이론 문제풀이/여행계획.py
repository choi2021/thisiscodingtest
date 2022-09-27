# #내풀이:
# #여행계획을 따를 수 있다는건 서로 연결되어있다, 서로 같은 부모를 갖는다고 볼 수 있다.
# #돌면서 서로 연결되어있는지를 체크


# n,m=map(int,input().split())
# graph=[]

# for i in range(n):
#   graph.append(list(map(int,input().split())))

# parent=[0]*n

# order=list(map(int,input().split()))

# for i in range(n):
#   parent[i]=i



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

# for i in range(n):
#   for j in range(n):
#     if graph[i][j]==1 and parent[i]!=parent[j]:
#       union_parent(parent,i,j)

# checked_parent=parent[order[0]]
# result="YES"
# for i in range(1,len(order)):
#   if checked_parent!=parent[order[i]]:
#     result="NO"
#     break


# print(result)

#책풀이

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

for i in range(1,n+1):
  parent[i]=i

for i in range(n):
  data=list(map(int,input().split()))
  for j in range(n):
    if data[j]==1:
      union_parent(parent,i+1,j+1)

plan=list(map(int,input().split()))
result=True
for i in range(m-1):
  if find_parent(parent,plan[i])!=find_parent(parent,plan[i+1]):
    result=False

if result:
  print("YES")
else:
  print("NO")