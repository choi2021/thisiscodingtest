
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

import sys
N,M=list(map(int,input().split()))
data=list(map(int,sys.stdin.readline().rstrip().split()))

start=0
end=max(data)


def binary_search(start,end):
  while (start<=end):
    mid=(start+end)//2
    total=0
    for i in data:
      if i-mid>0:
        total+=i-mid
    if total==M:
      return mid;
    elif total<M:
      end=mid-1
    else:
      start=mid+1
    
print(binary_search(start,end))