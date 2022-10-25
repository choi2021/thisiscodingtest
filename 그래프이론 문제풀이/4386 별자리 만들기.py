from itertools import combinations

n=int(input())
parent=[0]*(n+1)
points=[]
edges=[]

for i in range(n+1):
	parent[i]=i

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

for i in range(n):
	x,y=map(float,input().split())
	points.append((x,y,i))

for i in list(combinations(points,2)):
	f,s=i
	dist=((f[0]-s[0])**2+(f[1]-s[1])**2)**0.5
	edges.append((dist,f[2],s[2]))

edges.sort()
result=0
for edge in edges:
	dist,a,b=edge
	if find_parent(parent,a)!=find_parent(parent,b):
		result+=dist
		union_parent(parent,a,b)
print(f"{result:.2f}")
