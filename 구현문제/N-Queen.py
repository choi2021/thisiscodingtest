n=int(input())
graph=[[True]*n for _ in range(n)]

def possible_pos():
  for i in range(n):
    for j in range(n):
      if graph[i][j]==True:
        return (i,j)
  return (-1,-1)

def mark_False(x,y):
    for i in range(n):
      graph[i][y]=False
    for j in range(n):
      graph[x][j]=False
    for i in range(n):
      if 0<=i+x<n and 0<=i+y<n:
        graph[i+x][i+y]=False
      if 0<=-i+x<n and 0<=-i+y<n:
        graph[-i+x][-i+y]=False
      if 0<=i+x<n and 0<=-i+y<n:
        graph[i+x][-i+y]=False
      if 0<=-i+x<n and 0<=i+y<n:
        graph[-i+x][i+y]=False

answer=0
for i in range(n):
  for j in range(n):
    mark_False(i,j)
    result=True
    for _ in range(1,n):
      x,y=possible_pos()
      if x<0:
        result=False
        break
      mark_False(x,y)
    if result==True:
      answer+=1
  
print(answer)
    



