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

n=int(input())
array=list(map(int,input().split()))

d=[0]*100

d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
  d[i]=max(d[i-2]+array[i],d[i-1])

print(d[n-1])

