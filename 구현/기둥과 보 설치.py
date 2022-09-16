
n=int(input())
build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

#내풀이
#1.기둥과 보를 표시할 2차원 배열 만들기
#2. 빌드 프레임에 따라 표시
#테스트케이스 1번은 통과했지만 2번부터 오류가 나
#매번 체크해줘야 하는데 체크를 하지 않았어 

def solution(n, build_frame):
  col_table=[[0]*(n+1) for _ in range(n+1)]
  row_table=[[0]*(n+1) for _ in range(n+1)]
  col=[]
  row=[]
  for i in build_frame:
    x,y,a,b=i;
    if a==0:
      if b==1:
        col.append((x,y))  
        col_table[x][y]+=1
        col_table[x][y+1]+=1
        for i in col:
          px,py=i
          if y==0 or row_table[px][py]>0 or col_table[px][py]>0:
            continue
          else:
            col.remove((x,y))
            col_table[x][y]-=1
            col_table[x][y+1]-=1
            break           
      else:
        col.remove((x,y))
        col_table[x][y]-=1
        col_table[x][y+1]-=1
        for i in col:
          px,py=i
          if y==0 or row_table[px][py]>0 or col_table[px][py]>0:
            continue
          else:
            col.append((x,y))
            col_table[x][y]+=1
            col_table[x][y+1]+=1
            break
    elif a==1:
      if b==1:
        row.append((x,y))  
        row_table[x][y]+=1
        row_table[x+1][y]+=1
        for j in row:
          px,py=j
          if col_table[px][py] >0 or col_table[px+1][py]>0 or ( row_table[px-1][py] >0 and row_table[px+1][py]>0):
            continue
          else:
            row.remove((x,y))
            row_table[x][y]-=1
            row_table[x][y+1]-=1  
            break
      else:
        row.remove((x,y))
        row_table[x][y]-=1
        row_table[x][y+1]-=1  
        for j in row:
          px,py=j
          if col_table[px][py] >0 or col_table[px+1][py]>0 or ( row_table[px-1][py] >0 and row_table[px+1][py]>0):
            continue
          else:
            row.append((x,y))
            row_table[x][y]+=1
            row_table[x][y+1]+=1  
            break
  
  result=[]
  for i in col:
    x,y=i
    result.append([x,y,0])
  for j in row:
    x,y=j
    result.append([x,y,1])
  return sorted(result)

print(solution(n,build_frame))

# 책풀이

# def possible(answer):
#   for x, y, stuff in answer:
#     if stuff==0:
#       if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
#         continue
#       return False
#     elif stuff==1:
#       if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1]in answer and [x+1,y,1] in answer):
#         continue
#       return False
#   return True  
# def solution(n,build_frame):
#   answer=[]
#   for frame in build_frame:
#     x,y,stuff,operate=frame
#     if operate==0:
#       answer.remove([x,y,stuff])
#       if not possible(answer):
#         answer.append([x,y,stuff])
#     if operate ==1:
#       answer.append([x,y,stuff])
#       if not possible(answer):
#         answer.remove([x,y,stuff])
#   return sorted(answer)

# print(solution(n,build_frame))