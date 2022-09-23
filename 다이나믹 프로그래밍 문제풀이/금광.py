# #내풀이:
# #각 점에서 오른쪽으로 갈때 위,중간,아래 세가지 방향으로 값을 더했을 때 그값을 더해줘서 table을 갱신,
# # 방향중 내부가 아니면 pass, 위치를 계속 추적해서 값을 계산했어

# t=int(input())

# dy=[1,1,1]
# dx=[1,0,-1]

# for _ in range(t):
#   n,m=map(int,input().split())
#   graph=[[0]*m for i in range(n)]
#   d=[0]*m
#   data=list(map(int,input().split()))
#   for i in range(n):
#     for j in range(m):
#       graph[i][j]=data[i*m+j]

#   pos=(0,0)
#   for i in range(n):
#     if d[0]<graph[i][0]:
#       pos=(i,0)
#     d[0]=max(graph[i][0],d[0])


#   for i in range(1,m):
#     x,y=pos
#     for j in range(3):
#       if 0<=x+dx[j]<n:
#         if graph[x+dx[j]][i]+d[i-1]>d[i]:
#           pos=(x+dx[j],i)
#           d[i]=max(graph[x+dx[j]][i]+d[i-1],d[i])

#   print(d[m-1])


for tc in range(int(input())):
  n,m= map(int,input().split())
  array=list(map(int,input().split()))

  dp=[]
  index=0
  for i in range(n):
    dp.append(array[index:index+m]) # 이렇게 받을 수 있구나...  
    index+=m
  
  for j in range(1,m):
    for i in range(n):
      if i==0:
        left_up=0
      else:
        left_up=dp[i-1][j-1]
      if i==n-1:
        left_down=0
      else:
        left_down=dp[i+1][j-1]
      left=dp[i][j-1]
      dp[i][j]=dp[i][j]+max(left_up,left_down,left)
    
    result=0
    for i in range(n):
      result=max(result,dp[i][m-1])
    print(result)
      