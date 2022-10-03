# from itertools import permutations

# n,m=map(int,input().split())
# data=[i for i in range(1,n+1)]

# for perm in permutations(data,m):
#   for i in perm:
#     print(i, end=" ")
#   print()


n,m=map(int,input().split())
s=[]
visited=[False]*(n+1)

def dfs():
  if len(s)==m:
    print(" ".join(map(int,s)))
    return
  for i in range(1,n+1):
    if visited[i]:
      continue
    visited[i]=True
    s.append(i)
    dfs()
    s.pop()
    visited[i]=False