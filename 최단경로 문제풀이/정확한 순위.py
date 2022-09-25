# # 내풀이: 화살표방향은 작은 곳에서 큰 곳으로, 순위를 알 수 있다는 건 모든 지점에서 찾아갈 수 있다.
# # n<500이하이므로 플로이드 워셜 사용 가능

# INF=int(1e9)
# n,m=map(int,input().split())
# graph=[[INF]*(n+1) for i in range(n+1)]

# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if i==j:
#       graph[i][j]=0

# for i in range(m):
#   a,b=map(int,input().split())
#   graph[a][b]=1


# for k in range(1,n+1):
#   for i in range(1,n+1):
#     for j in range(1,n+1):
#       graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

# result=0

# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if graph[i][j]==INF:
#       print(0, end=" ")
#       continue
#     print(graph[i][j],end=" ")
#   print()

# # for i in range(1,n+1):
# #   count=0
# #   for j in range(1,n+1):
# #     if graph[i][j]!=INF or graph[j][i]!=INF:
# #       count+=1
# #   if count==n:
# #     result+=1
# # print(result)

# 책풀이

INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

for _ in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

result=0

for i in range(1,n+1):
  count=0
  for j in range(1,n+1):
    if graph[i][j]!=INF or graph[j][i]!=INF:
      count+=1
  if count==n:
    result+=1
print(result)