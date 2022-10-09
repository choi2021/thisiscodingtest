from collections import deque
n,k=map(int,input().split())
visited=[False]*1000001
result=1e9

# def bfs():
#   global result
#   q=deque([(n,0)])
#   visited[n]=True
#   while q:
#     pos,time=q.popleft()

#     if pos<0 or pos*2>1000000:
#       continue
  
#     if pos==k:
#       result=min(time,result)
#       continue
#     if visited[pos*2]==False:
#       q.append((pos*2,time+1))
#       visited[pos*2]=True
#     if visited[pos+1]==False:  
#       q.append((pos+1,time+1))
#       visited[pos*2]=True
#     if visited[pos-1]==False:  
#       q.append((pos-1,time+1))
#       visited[pos*2]=True
# bfs()
# print(result)
