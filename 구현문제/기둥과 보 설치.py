#기둥: 바닥위,보의 한쪽끝, 다른기둥위, 위쪽으로
#보: 한쪽끝이 기둥위, 양쪽 끝이 다른 보, 오른쪽으로

n=5
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def solution(n, build_frame):
  graph=[[0]*(n+1) for _ in range(n+1)]
  parts=[]
  
  for frame in build_frame:
    x,y,a,b=frame
    if b==1:
      parts.append((x,y,a))
      result=True
      for part in parts:
        px,py,t=part
        if a==0:
          if y==0 or (x,y,1) in parts or (x-1,y,1) in parts or (x,y-1,0) in parts:
            continue
          else:
            result=False
            break
        if a==1:
          if (x,y-1,0) in parts or (x+1,y-1,0) in parts or ((x+1,y,1) in parts and (x-1,y,1) in parts):
            continue
          else:
            result=False
            break
      if result!=True:
        parts.remove((x,y,a))
    elif b==0:
      parts.remove((x,y,a))
      result=True
      for part in parts:
        px,py,t=part
        if t==0:
          if py==0 or (px,py,1) in parts or (px-1,py,1) in parts or (px,py-1,0) in parts:
            continue
          else:
            result=False
            break
        if t==1:
          if (px,py-1,0) in parts or (px+1,py-1,0) in parts or ((px+1,py,1) in parts and (px-1,py,1) in parts):
            continue
          else:
            result=False
            break
      if result!=True:
        parts.append((x,y,a))
  
  parts.sort(key=lambda x:(x[0],x[1],x[2]))
  return  parts

print(solution(n,build_frame))

# 책풀이:
def possible(answer):
  for x,y,stuff in answer:
    if stuff==0:
      if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
        continue
      return False
    elif stuff==1:
      if [x,y-1,0] in answer or [x+1,y-1,0] in answer or([x-1,y,1] in answer and [x+1,y,1] in answer):
        continue
      return False
    return True

def solution(n,build_frame):
  answer=[]
  for frame in build_frame:
    x,y,stuff,operate=frame
    if operate==0:
      answer.remove([x,y,stuff])
      if not possible(answer):
        answer.append([x,y,stuff])
    if operate==1:
      answer.append([x,y,stuff])
      if not possible([x,y,stuff]):
        answer.remove([x,y,stuff])
  return sorted(answer)
