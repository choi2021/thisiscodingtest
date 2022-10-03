n,m=map(int,input().split())
s=[]
visited=[False]*(n+1)

def dfs():
  if len(s)==m:
    print(" ".join(map(str,s)))
  for i in range(1,n+1):
    if visited[i]==True or (len(s)!=0 and s[-1]>i):
      continue
    s.append(i)
    visited[i]=True
    dfs()
    s.pop()
    visited[i]=False

dfs()