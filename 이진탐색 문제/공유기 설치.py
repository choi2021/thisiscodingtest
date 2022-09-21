# 1. n이 20만이기 떄문에 이진탐색을 써야해, 모든 경우의 수를 계산할 수는 없어
#

# n,c=map(int,input().split())
# data=[]
# for _ in range(n):
#   data.append(int(input()))
# data.sort()

# start=0
# end=n-1
# result=-1
# while start<=end:
#   mid=(start+end)//2
#   avg=data[start]+data[end]/c
#   if mid>avg:
#     end=mid-1
#   elif mid<=avg:
#     result= mid

# print(result)


# 2.책풀이
# 최소 거리와 최대 거리 중간값을 이용해서 중간값보다 큰 공유기만 받아들여질 수 있어
# 이런 문제의 키는 기준점인데, 기준점은 따로 주어지니까 그걸 좀 더 깊이 생각해보자 

n,c=list(map(int,input().split()))

array=[]
for _ in range(n):
  array.append(int(input()))
array.sort()

start=1
end=array[-1]-array[0]
result=0

while (start<=end):
  mid=(start+end)//2
  value=array[0]
  count=1
  for i in range(1,n):
    if array[i]>=value+mid:
      count+=1
  if count>=c:
    start=mid+1
    result=mid
  else:
    end=mid-1
