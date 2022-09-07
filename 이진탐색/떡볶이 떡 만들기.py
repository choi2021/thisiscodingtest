
# N,M=list(map(int,input().split()))
# items=list(map(int,input().split()))

# max_height=max(items)
# height_arr=[x for x in range(0,max_height)]

# def binary_search(array,start,end):
#   mid=(start+end)//2
#   sum=0
#   for i in items:
#     diff=i-array[mid]
#     if diff>=0:
#       sum+=diff
#   if sum==M:
#     return array[mid]
#   elif sum>M:
#     return binary_search(array,mid+1,end)
#   else:
#     return binary_search(array,start,mid-1)

# print(binary_search(height_arr,0,max_height-1))



# 답안 풀이

n,m=list(map(int,input().split(" ")))
array=list(map(int,input().split()))

start=0
end=max(array)

result=0
while(start<=end):
  total=0
  mid=(start+end)//2
  for x in array:
    if x>mid:
      total+=x-mid
  if total<m:
    end=mid-1
  else:
    result=mid
    start=mid+1

print(result)