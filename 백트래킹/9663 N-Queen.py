# BFS를 이용해서 풀어보려했지만 어디서 잘못되었는지도 이해하기 힘들어
# from collections import deque
# n=int(input())
# graph=[0]*n
# total=0

# dx=[1,0,-1,0,1,-1,1,-1]
# dy=[0,1,0,-1,1,1,-1,-1]

# def attack(pos,i):
#   x,y=pos
#   q=deque([(x,y)])
#   while q:
#     x,y=q.popleft()
#     nx=x+dx[i]
#     ny=y+dy[i]
#     if 0<=nx<n and 0<=ny<n:
#       if graph[nx][ny]==0:
#         q.append((nx,ny))
#       else:
#         return False
#   return True

# def dfs(num):
#   global total
#   if num==n:
#     for queen in queens:
#       for i in range(8):
#         if attack(queen,i)==False:
#           return
#     total+=1
#   for i in range(1,n+1):
#       if graph[i][j]==0:
#         graph[i][j]=1
#         dfs(num+1)
#         graph[i][j]=0

# dfs(0)
# print(total)

#백트래킹
# 1. 행을 고려하지 않는 이유는 위에서 부터 차례로 하나의 행에는 하나의 퀸만 놓을 거기 때문에
# 2. 열과 대각선만 고려해서 같은 열에 있는 지 체크
# 3. 일차원 배열로 graph[i]=j라면 (i,j)에 퀸을 두었다는 뜻 


n=int(input())
ans=0
row=[0]*n

def check(x):
  for i in range(x):
    if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
      return False
  return True

def n_queens(x):
  global ans
  if x==n:
    ans+=1
    return
  else:
    for i in range(n):
      row[x]=i
      if check(x):
        n_queens(x+1)

n_queens(0)
print(ans)