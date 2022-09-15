# # 1. 현재 방향에 따라 좌우 방향전환을 위한 테이블 만들기
# # 2. 전달받은 move값 전까지는 같은 방향으로 계속 움직여
# # 3. 전달받은 값이되면 회전하기

# N=int(input())
# K=int(input())

# game_data=[[0]*N for i in range(N)]

# for _ in range(K):
#   r,c=map(int,input().split())
#   game_data[r-1][c-1]=1

# L=int(input())
# moves=[]
# for _ in range(L):
#   X,C=input().split()
#   moves.append((int(X),C))

# body=[(0,0),(0,0)]
# length=1

# dx=[+1,0,-1,0]
# dy=[0,+1,0,-1]

# def snake():
#   direction=0
#   time=0
#   for i in moves:
#     for j in range(i[0]):
#       nx=body[0][0]+dx[direction]
#       ny=body[0][1]+dy[direction]
#       time+=1
#       if nx>=N or nx<0 or ny>=N or ny<0:
#         return time 
#       if (nx,ny) in body:
#         return time
#       if game_data[nx][ny]!=1:
#         body[0]=(nx,ny)
#         tailX,tailY=body.pop()
#         body.append((tailX+dx[direction],tailY+dy[direction]))
#       else:
#         game_data[nx][ny]=0
#         for m in range(1,len(body)-1):
#           body[m]=(body[m][0]+dx[direction] ,body[m][1]+dy[direction])

#     if i[1]=="D":
#       direction+=(direction+1)%4
#     else:
#       direction-=(direction-1)%4

# print(snake())

#책풀이

n = int(input())
k = int(input())
graph = [[0] * (n+1) for _ in range(n+1)] # 맵 정보

# 맵 정보 (사과가 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

info = [] # 방향 회전 정보

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = map(str, input().split())
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4

    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    graph[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1<=nx and nx<=n and 1<=ny and ny<=n and graph[nx][ny] != 2:
            
            # 사과가 없다면 이동 후에 꼬리 제거
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                graph[px][py] = 0
            
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append((nx, ny))
        
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        
        # 회전할 시간인 경우 회전
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time

print(simulate())