#1.내풀이: BFS라는건 이해했지만 방문처리와 회전에서 막혔어..
# from collections import deque

# dx=[1,-1,0,0]
# dy=[0,0,1,-1]

# degree=[-90,-180,-270,90,180,270]

# def rotate(deg,axis,pos,board):
#     rad = deg * (math.pi / 180.0)
#     ax,ay=axis
#     x,y=pos
#     nx = round(math.cos(rad)*x - math.sin(rad)*y)+ax
#     ny = round(math.sin(rad)*x + math.cos(rad)*y)+ay
#         if board[round(math.cos(rad/2)*x - math.sin(rad/2)*y)+ax][round(math.sin(rad/2)*x + math.cos(rad/2)*y)+ay]==1:
#             return  
#         else:
#             return (nx,ny)
            

# def bfs(pos,board):
#     n=len(board)
#     q=deque()
#     q.append(pos)
#     while q:
#         pos1,pos2=q.popleft()
#         x1,y1=pos1
#         x2,y2=pos2
#         for i in range(4):
#             nx1=x1+dx[i]
#             ny1=y1+dy[i]
#             nx2=x2+dx[i]
#             ny2=y2+dy[i]
#             if nx1<0 or nx1>n or nx2<0 or nx2>n:
#                 continue
#             if board[nx1][ny1]==0 and board[nx2][ny2]==0:
#                 board[nx1][ny1]=board[x1][y1]-1
#                 board[nx2][ny2]=board[x2][y2]-1
#                 q.append([(nx1,ny1),(nx2,ny2)])
#         for i in range(6):
#             for 
        
#     print(board)
#     return board[n-1][n-1] 
    

# def solution(board):
#     print(bfs([(0,0),(0,1)],board))
    
# 책풀이

from collections import deque

def get_next_pos(pos,board):
  next_pos=[]
  pos=list(pos)
  pos1_x,pos1_y,pos2_x,pos2_y=pos[0][0],pos[0][1],pos[1][0],pos[1][1]
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]

  for i in range(4):
    pos1_next_x,pos1_next_y,pos2_next_x,pos2_next_y=pos1_x+dx[i], pos1_y+dy[i],pos2_x+dx[i],pos2_y+dy[i]
    if board[pos1_next_x][pos1_next_y]==0 and board[pos2_next_x][pos2_next_y]==0:
      next_pos.append({(pos1_next_x,pos1_next_y),(pos2_next_x,pos2_next_y)})
    if pos1_x==pos2_x:
      for i in [-1,1]:
        if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0:
          next_pos.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)})
          next_pos.append({(pos2_x,pos2_y),(pos2_x+i,pos2_y)})
    elif pos1_y==pos2_y:
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
  q.append((pos,0))
  visited.append(pos)

  while q:
    pos,cost=q.popleft()
    if (n,n) in pos:
      return cost
    for next_pos in get_next_pos(pos,new_board):
      if next_pos in get_next_pos(pos,new_board):
        if next_pos not in visited:
          q.append((next_pos,cost+1))
          visited.append(next_pos)
  return 0