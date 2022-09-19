# 내풀이: DFS를 쓰려했지만 결과를 반환 못해서 실패..., O만 아니면 계속 관측해야하는데 다른 조건들: T, X를 W로 바꾸기등을 해서 더 헷갈렸어
# #1.DFS로 모든 경우의 수를 체크해서 확인가능 (N이 최대 6)
# #2.먼저 3개의 장애물을 설치 
# #3.T를 중심으로 빈곳들을 상하좌우 체크할 때, 벽이 있으면 탐지 그만, 학생이면 전체 멈추기


# N=int(input())
# graph=[]
# for _ in range(N):
#   graph.append(input().split())
# temp=[["x"]*N for _ in range(N)]

# dx=[1,-1,0,0]
# dy=[0,0,1,-1]

# for i in range(N):
#   for j in range(N):
#     if graph[i][j]=="S" or graph[i][j]=="T":
#       temp[i][j]=graph[i][j]

# def watch(x,y):
#   for dir in range(4):
#     if dir==0:
#       while y>=0:
#         if temp[x][y]=="S":
#           return True
#         if temp[x][y]=="O":
#           return False
#         y-=1
#     if dir==1:
#       while y<N:
#         if temp[x][y]=="S":
#           return True
#         if temp[x][y]=="O":
#           return False
#         y+=1
#     if dir==2:
#       while x>=0:
#         if temp[x][y]=="S":
#           return True
#         if temp[x][y]=="O":
#           return False
#         x-=1
#     if dir==3:
#       while x<N:
#         if temp[x][y]=="S":
#           return True
#         if temp[x][y]=="O":
#           return False
#         x+=1
#     return False


# result=False

# def dfs(count):
#   global result
#   if count==3:
#     for i in range(N):
#       for j in range(N):
#         temp[i][j]=graph[i][j]
#     for i in range(N):
#       for j in range(N):
#         if temp[i][j]=="T":
#           if watch(i,j)==True:
#             result=True
#             return
#   for i in range(N):
#     for j in range(N):
#       if graph[i][j]=="X":
#         graph[i][j]="O"
#         count+=1
#         dfs(count)
#         graph[i][j]="X"#  백트래킹 기법
#         count-=1#백트래킹 기법

# print(dfs(0))
  
  
#DFS 다른 사람 풀이
n = int(input())
graph = []
teacher = 0
for _ in range(n):
  data = list(input().strip().split(' '))
  teacher += data.count('T')
  graph.append(data)

# 상,하,좌,우 움직이는 배열
dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

# 직선 방향 확인 함수
def check_S(x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 직선 방향으로 확인
    while 0<= nx < n and 0<= ny < n and graph[nx][ny] !='O':
      if graph[nx][ny] == 'S':
        # 감시가능하다
        return True            
      else:        
        # T 나 X으면 계속 탐색
        nx += dx[i]
        ny += dy[i]
  # 감시 불가능하다
  return False

def solution(count):
  global answer
  if count == 3:
    cnt = 0
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 'T':
          if not check_S(i,j):          
            cnt+=1
    # 모든 선생이 감시가 불가능할 때
    if cnt == teacher:
      answer = True
    return

  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'X':
        graph[i][j] = 'O'
        count +=1
        solution(count)
        graph[i][j] = 'X'
        count -=1

answer = False
solution(0)
if answer:
  print('YES')
else:
  print('NO')


# # 책풀이
# from itertools import combinations

# n=int(input())
# board=[]
# teachers=[]
# spaces=[]

# for i in range(n):
#   board.append(list(input().split()))
#   for j in range(n):
#     if board[i][j]=="T":
#       teachers.append((i,j))
#     if board[i][j]=="X":
#       spaces.append((i,j))

# def watch(x,y,direction):
#   if direction==0:
#     while y>=0:
#       if board[x][y]=="S":
#         return True
#       if board[x][y]=="O":
#         return False
#       y-=1
#   if direction==1:
#     while y<n:
#       if board[x][y]=="S":
#         return True
#       if board[x][y]=="O":
#         return False
#       y+=1
#   if direction==2:
#     while x>=0:
#       if board[x][y]=="S":
#         return True
#       if board[x][y]=="O":
#         return False
#       x-=1
#   if direction==3:
#     while x<n:
#       if board[x][y]=="S":
#         return True
#       if board[x][y]=="O":
#         return False
#       x+=1
#   return False

# def process():
#   for x, y in teachers:
#     for i in range(4):
#       if watch(x,y,i):
#         return True
#   return False

# find=False

# for data in combinations(spaces,3):
#   for x, y in data:
#     board[x][y]="O"
#   if not process():
#     find=True
#     break
#   for x,y in data:
#     board[x][y]="X"
# if find:
#   print("YES")
# else:
#   print("NO")
