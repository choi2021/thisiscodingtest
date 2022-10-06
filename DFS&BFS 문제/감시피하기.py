# 1.백트레킹으로 우선 3개의 장애물을 설치해
# 2. 선생님을 BFS로 탐색하게 해서 학생을 찾으면 False 못찾으면 True /bfs에서 문제가 나서 못풀었어
# 3. 결과에 따라 Yes, no
n=int(input())
graph=[]
teacher=[]
for i in range(n):
  graph.append(list(input().split()))
  for j in range(n):
    if graph[i][j]=="T":
      teacher.append((i,j))

result=False
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs():
  for x,y in teacher:
    for i in range(4):
      while 0<=x<n and 0<=y<n:
        if graph[x][y]=="O":
          break
        if graph[x][y]=="S":
          return False
        x+=dx[i]
        y+=dy[i]
  return True
    

def backTracking(num):
  global result
  if num==3:
    if bfs():
      result=True
    return 

  else:
    for i in range(n):
      for j in range(n):
        if graph[i][j]=="X":
          graph[i][j]="O"
          backTracking(num+1)
          graph[i][j]="X"

backTracking(0)
if result:
  print("YES")
else:
  print("NO")