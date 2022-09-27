# # 내풀이:
# # 탑승구 정보를 오름차순으로 정렬한 후에 탑승구 번호를 올려가면서 번호보다 크거나 같으면 count를 늘려간다.
# import sys
# input=sys.stdin.readline
# g=int(input())
# p=int(input())

# entries=[0]*(p+1)

# for i in range(1,p+1):
#   entries[i]=int(input())

# count=0


#책풀이: 서로소 집합을 이용해, 도킹을 못할때는 루트가 0일때, 더이상 도킹을 할 수 없다는 의미
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

g=int(input())
p=int(input())
parent=[0]*(g+1)

for i in range(1,g+1):
  parent[i]=i

result=0
for _ in range(p):
  data=find_parent(parent,int(input()))
  if data==0:
    break
  union_parent(parent,data,data-1)
  result+=1

print(result)