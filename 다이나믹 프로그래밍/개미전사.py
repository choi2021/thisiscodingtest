# N=int(input())
# data=list(map(int,input().split()))
# d=[0]*(N)

# for i in range(0,N):
#   if i==0:
#     d[i]=data[i]
#   elif i==1:
#     d[i]=max(data[0],data[1])
#   d[i]=max(d[i-2]+data[i],d[i-1])


# print(max(d))

# 풀이
N=int(input())
data=list(map(int,input().split()))

d=[0]*100
d[0]=data[0]
d[1]=max(data[0],data[1])

for i in range(2,N):
  d[i]=max(data[i]+d[i-2],d[i-1])

print(d[N-1])


