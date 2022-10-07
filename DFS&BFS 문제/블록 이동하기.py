# 1. 로봇의 두좌표는 함께 움직여야해
# 2. 회전을 구현하기 어려워

# from collections import deque



# def turn_left(pivot,direction):
#   x,y=pivot
#   if graph[]

# # def turn_right(pivot):

# dx=[1,0,-1,0]
# dy=[0,1,0,-1]

# def solution(board):
#   n=len(board)
#   visited=[[0]*n for _ in range(n)]
#   q=deque([((0,0),(0,1))])
#   visited[0][0]+=1
#   visited[0][1]+=1
#   time=0
#   while q:
#     print(q)
#     now_pos=q.popleft()
#     now1=now_pos[0]
#     now2=now_pos[1]
#     for i in range(4):
#       nx1=now1[0]+dx[i]
#       ny1=now1[1]+dy[i]
#       nx2=now2[0]+dx[i]
#       ny2=now2[1]+dy[i]
#       if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n:
#         if board[nx1][ny1]!=1 and  board[nx2][ny2]!=1 and visited[nx1][ny1]<2 and visited[nx2][ny2]<2:
#           visited[nx1][ny1]+=1
#           visited[nx2][ny2]+=1
#           q.append(((nx1,ny1),(nx2,ny2)))
#           time+=1
#     for i in range(4):
#       nx2=now1[0]+dx[i]
#       ny2=now1[1]+dy[i]
#       if 

# solution(board)


board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

from collections import deque

def get_next_pos(pos,board):
  next_pos=[]
  pos=list(pos)
  pos1_x,pos1_y,pos2_x,pos2_y=pos[0][0],pos[0][1],pos[1][0],pos[1][1]
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  for i in range(4):
    pos1_next_x, pos1_next_y,pos2_next_x,pos2_next_y=pos1_x+dx[i],pos1_y+dy[i],pos2_x+dx[i],pos2_y+dy[i]
    if board[pos1_next_x][pos1_next_y]==0 and board[pos2_next_x][pos2_next_y]==0:
      next_pos.append({(pos1_next_x,pos1_next_y),(pos2_next_x,pos2_next_y)})
  if pos1_x==pos2_x:# 가로로 놓여있어, 위나 아래로 회전시켜
    for i in [-1,1]:
      if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0: #위 두칸이 모두 비어있을 때
        next_pos.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)})
        next_pos.append({(pos2_x,pos2_y),(pos2_x+i,pos2_y)})
  elif pos1_y==pos2_y: #세로로 놓여있어, 위나 아래로 회전시켜
    for i in [-1,1]:
      if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0:
        next_pos.append({(pos1_x,pos1_y),(pos1_x,pos1_y+i)})
        next_pos.append({(pos2_x,pos2_y),(pos2_x,pos2_y+i)})
  return next_pos

def solution(board):
  n=len(board)
  new_board=[[1]*(n+2) for _ in range(n+2)]
  for i in range(n):
    for j in range(n):
      new_board[i+1][j+1]=board[i][j]
  
  q=deque()
  visited=[]
  pos={(1,1),(1,2)}
  q.append((pos,0)) #시간을 같이 넣어
  visited.append(pos)
  while q:
    pos,cost=q.popleft()
    if (n,n) in pos:
      return cost
    for next_pos in get_next_pos(pos,new_board):
      if next_pos not in visited:
        q.append((next_pos,cost+1))
        visited.append(next_pos)
  return 0

  solution()
