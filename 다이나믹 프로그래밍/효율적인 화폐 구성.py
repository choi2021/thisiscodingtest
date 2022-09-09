# 내풀이

# N,M=list(map(int,input().split()))
# money=[]

# d=[-1]*10001

# for i in range(N):
#   money.append(int(input()))

# for i in range(1,M+1):
#     if min(money)>i:
#       continue
#     if i in money:
#       d[i]=1
#       continue
#     min_val=10000
#     for unit in money:
#       if i-unit<0 or d[i-unit]<0:
#         continue
#       if d[i-unit]+1<min_val:
#         min_val=d[i-unit]+1
#     if min_val!=10000:
#       d[i]=min_val

# print(d[M])


# 책풀이

n,m=map(int,input().split())
array=[]
for i in range(n):
  array.append(int(input()))

d=[10001]*(m+1)

d[0]=0
for i in range(n):
  for j in range(array[i],m+1):
    if d[j-array[i]]!=10001:
      d[j]=min(d[j],d[j-array[i]]+1)

if d[m]==10001:
  print(-1)
else:
  print(d[m])