# #내풀이: dp table을 만들고 각 점에서 왼쪽과 오른쪽에서 값을 받아서 큰 값을 업데이트해줘

# n=int(input())
# graph=[]
# d=[]
# for i in range(n):
#   graph.append(list(map(int,input().split())))

# for i in range(n):
#   row=[]
#   for j in range(len(graph[i])):
#     row.append(graph[i][j])
#   d.append(row)

# for i in range(1,n):
#   for j in range(len(graph[i])):
#     if j-1<0:
#       left=0
#     else:
#       left=d[i-1][j-1]
#     if j>=len(graph[i-1]):
#       right=0
#     else:
#       right=d[i-1][j]
    
#     d[i][j]=d[i][j]+max(left,right)

# print(max(d[n-1]))


# 책풀이

n=int(input())
dp=[]

for _ in range(n):
  dp.append(list(map(int,input().split())))

for i in range(1,n):
  for j in range(i+1):
    if j==0:
      up_left=0
    else:
      up_left=dp[i-1][j-1]
    if j==i:
      up=0
    else:
      up=dp[i-1][j]
    dp[i][j]=dp[i][j]+max(up_left,up)

print(max(dp[n-1]))