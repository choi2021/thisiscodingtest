# 내풀이
# 1. i번째 값은 i-k(화폐 단위)한 값+1로 나타낼 수 있어

# n,m=map(int,input().split())
# coins=[]
# d=[10001]*(m+1)
# for i in range(n):
#   coins.append(int(input()))

# d[0]=0

# for i in range(min(coins),m+1):
#   for coin in coins:
#     d[i]=min(d[i-coin]+1,d[i])
#   print(d[i],i)

# if d[m]==10001:
#   print(-1)
# else:
#   print(d[i])

#책풀이
#생각은 동일했지만 구현이 아직 내가 부족해
#똑같이 i번째 값은 i-k(화폐 단위)한 값+1로 나타낼 수 있어

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
