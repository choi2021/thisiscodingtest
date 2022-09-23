# # 내풀이: 날짜 처리에 어려워하다가 포기

# n=int(input())
# data=[]
# d=[0]*n

# for _ in range(n):
#   t,p=map(int,input().split())
#   data.append((t,p))

# for i in range(n):
#   time=0
#   for j in range(i+1):
#     t,p=data[j]
#     if j+t<=i:
#       d[i]=max(d[i],d[j]+p)
#       time+=t
# print(data)

# 책풀이: 앞에서부터 카운트 하지 않고 뒤에서 부터 세서 가능한 경우들을 체크했어
n=int(input())
t=[]
p=[]
dp=[0]*(n+1)
max_value=0

for _ in range(n):
  x,y=map(int,input().split())
  t.append(x)
  p.append(y)


for i in range(n-1,-1,-1):
  time=t[i]+i
  if time<=n:
    dp[i]=max(p[i]+dp[time],max_value)
    max_value=dp[i]
  else:
    dp[i]=max_value

print(max_value)