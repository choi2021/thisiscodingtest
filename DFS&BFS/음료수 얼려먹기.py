from posixpath import split


N,M=map(int,input().split())

graph=[]

for _ in range(N):
  graph.append(list(map(int,input())))

result=0

def BFS(x,y): #각 자리마다 체크
  if x<0 or y<0 or x>=N or y>=M:
    return False
  if graph[x][y]==0:
    graph[x][y]=1
    BFS(x-1,y)
    BFS(x+1,y)
    BFS(x,y-1)
    BFS(x,y+1)
    return True
  return False

for i in range(N):
  for j in range(M):
    if BFS(i,j):
      result+=1
print(result)
